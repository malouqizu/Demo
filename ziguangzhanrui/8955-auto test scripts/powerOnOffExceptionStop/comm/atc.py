#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import serial
import ctypes
import datetime
from ctypes import *
from socket import *
import win32ras
import re
import subprocess

COMPORT = 'COM4'

class AtConfig(object):
    """ AT test configuration through env variables
    """

    def __init__(self):
        self.log_file_name = os.environ.get('AT_TEST_LOG_FILE', 'log.txt')
        self.com_port = COMPORT
        self.echo_server = os.environ.get("AT_TEST_ECHO_SERVER", "111.205.140.137")
        self.echo_port = int(os.environ.get("AT_TEST_ECHO_PORT", "11008"))
        self.relay_channel = int(os.environ.get("AT_TEST_RELAY_CHANNEL", "1"))
        self.relay_server = os.environ.get('AT_TEST_RELAY_SERVER', 'localhost')
        self.relay_port = int(os.environ.get('AT_TEST_RELAY_PORT', "9999"))
        self.entry_name = os.environ.get('AT_TEST_PPP_ENTRYNAME', '拨号连接')
        self.ping_addr = os.environ.get('AT_TEST_PING_ADDR', '123.57.221.42')
        self.local_conn_addr = os.environ.get('AT_TEST_LOCAL_CONN_ADDR', '10.102.21.1')


""" Global object """
atConfig = AtConfig()


class AtLogger(object):
    """ Simple logger for AT
        * support both stdout and log file
        * auto add prefix
    """
    #构造方法，也可以解释为初始化方法
    #在创建对象时执行此函数
    def __init__(self):
        self.fh = None
        try:
            #创建log_file_name文件，如果存在将文件长度清0，如果不存在将创建该文件
            #如果没有对log文件名进行设置，那么根据下面__write函数的分析，就直接将log输出到控制台
            self.fh = open(atConfig.log_file_name, 'w')
        except:
            self.fh = None
        #获取当前的时间戳
        self.start_time = time.time()

    #析构函数，在两种情况下被触发
    #1.Python解释器会默认调用此方法对创建的对象进行删除。
    #2.开发者在程序中手动使用del进行对对象的删除时进行调用。
    #这里可以认为是对__del__的重写，将log文件描述符关闭以节省资源。
    def __del__(self):
        if self.fh is not None:
            self.fh.close()

    def __write(self, out):
        ##如果没有对log文件名进行设置，那么就没有相应的log文件描述符，就直接将log输出到控制台
        if self.fh is not None:
            self.fh.write(out)
            #将通过write函数写入到内存的数据直接输出到文件，不使用缓冲区进行缓冲，这里指直接输出到log文件
            self.fh.flush()
        sys.stdout.write(out)

    def get_resp(self, line):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]<<< %s\n" % (stamp, line.strip()))

    def send_cmd(self, line):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]>>> %s\n" % (stamp, line.strip()))

    def case_start(self, name):
        self.__write('\n')
        self.__write("=== %s [start] ===\n" % (name.strip()))

    def case_end(self, name):
        self.__write("=== %s [end] ===\n" % (name.strip()))
        self.__write('\n')

    def case_log(self, line):
        self.__write("--- %s\n" % (line.strip()))

    def case_timed_log(self, line):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]--- %s\n" % (stamp, line.strip()))


""" Global object """
atLogger = AtLogger()
#现在重新对测试用例进行分析，对测试用例的执行场景有一个清晰的认识
#根据对示例代码的分析，执行场景主要有两种
#1.发送命令，有响应，对响应进行分析。
#根据昨天的分析，可以得出以下几种响应类型：
#1.1查询命令返回值：一般先包含一行或者多行设置值，最后一行为0k，这样就代表命令基本执行成功了。
#特征：最少返回两行字符串，最后一行为OK字符串。
#1.2设置命令返回值：一般只包含一行，这一行值为OK字符串。
#1.3发送数据命令返回值：一般返回一行，且为提示符>
#1.4命令执行错误返回值：一般为只有一行，且以+CME ERROR:开头
#1.5还有其他类型，关于他们的判断可以在相应的代码里面直接进行添加。
#2.直接等待响应。
#2.1等待响应直到包含某一行

#根据上面的分析基本上都是以行为单位进行判断
#那么将响应用列表进行存储，每个元素为响应的一行
#因此所有的判断就是对行的判断
#因此，跟具上面的分析，就可以写出针对行判断功能的不同函数
#__check_line(line):判断是否是期望的行
#_check_contain_line(line):判断一行里面是否有期望的字符串
#__check_expect(self, line, check):调用上面的函数，封装成一个通用的判断函数接口
#has(self, expected):
#contain(self, line):
#has_in_order(self, *expected):
#__read_resp(self, timeout, expected):
#send(self, cmd, timeout):
#wait(self, line, timeout):
#send_ok(self, cmd, timeout):
#__check_ok_error(line):判断一行是否具有OK，error，close OK，send OK等表示响应结束的字符串。
#get_line_starts(self, line):
#get_uptime(self):
#get_csq(self):

class AtChat(object):
    line_checked = ''
    line_contain_checked = ''
    ECHO = 0
    OK = 1
    ERROR = 2

    def __init__(self):
        self.port = atConfig.com_port
        self.baudrate = 115200
        self.bytesize = serial.EIGHTBITS
        self.parity = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE
        self.xonxoff = False
        self.rtscts = False
        self.dsrdtr = False
        self.timeout = 0.5
        self.write_timeout = 1.0

        self.serial = None
        self.coding = 'utf-8'

        #self.serial = None
        #初始化一个字节数组，如果参数为0，则返回为0个元素的字节数组
        self.inparsing = bytearray()
        #将响应以列表的形式进行保存，每个元素为一行
        self.resp = []
        self.last_cmd = ''

    @staticmethod
    def __check_line(line):
        return AtChat.line_checked == line

    @staticmethod
    def _check_contain_line(line):
        return AtChat.line_contain_checked in line

    def __check_expect(self, line, check):
        """ Check a line. The condition can be
            * integer (OK, ERROR, ECHO)
            * string: match a line
            * callable: return True/False
        """
        if callable(check):
            return check(line)
        elif type(check) == int:
            if check == self.ECHO:
                return line == self.last_cmd
            elif check == self.OK:
                return line == 'OK' or line == 'CLOSE OK' or line == 'SEND OK'
            elif check == self.ERROR:
                return line.startswith('+CME ERROR:')
        elif type(check) == str:
            return line == check
        return False

    def has(self, expected):
        """ Whether responses has the specified line
        """
        for res in self.resp:
            if self.__check_expect(res, expected):
                return True
        return False

    def contain(self, line):
        """Whether responses contain line
        """
        AtChat.line_contain_checked = line
        for res in self.resp:
            if self.__check_expect(res, AtChat._check_contain_line):
                return True
        return False

    def has_in_order(self, *expected):
        """ Whether the sequence appears in order
        """
        count = len(expected)
        n = 0
        check = expected[n]
        for res in self.resp:
            if self.__check_expect(res, check):
                n += 1
                if n == count:
                    break
                check = expected[n]
        return n == count

    @staticmethod
    def __check_ok_error(line):
        return line == 'OK' or line.startswith('+CME ERROR:') or line.startswith('>') or \
                 line.startswith('CLOSE OK') or line.startswith('SEND OK')

    def get_line_starts(self, line):
        """ Return the first response started with line
        """
        for res in self.resp:
            if res.startswith(line):
                return res
        return None

    def open(self):
        """ Open the serial port, and start a thread to read from the serial port
        """
        if self.serial is not None:
            return

        self.serial = serial.Serial(port=self.port,
                                    baudrate=self.baudrate,
                                    parity=self.parity,
                                    stopbits=self.stopbits,
                                    xonxoff=self.xonxoff,
                                    rtscts=self.rtscts,
                                    dsrdtr=self.dsrdtr,
                                    timeout=self.timeout,
                                    write_timeout=self.write_timeout)

    def close(self):
        """ Close the serial port
        """
        self.serial.close()
        self.serial = None

    def reopen(self):
        """ Reopen the serial port
        """
        if self.serial is not None:
            self.close()
        self.open()

    def sleep(self, seconds):
        """ Helper function to sleep a while, and always return True
        """
        time.sleep(seconds)
        return True

    def __read_resp(self, timeout, expected):
        """ Read responses till timeout or expected is satisfied
        """
        if timeout is not None:
            self.endtime = time.time() + timeout

        while True:
            if timeout is not None and time.time() > self.endtime:
                return False

            #这些读数据的代码谢的非常有意思，也非常的符合逻辑性
            #是对命令的响应值有着非常准确的分析，并对其进行了详细的
            #分类
            #1.查询命令返回值：一般先包含一行或者多行设置值，最后一行为0k，这样就代表命令基本执行成功了。
            #特征：最少返回两行字符串，最后一行为OK字符串。
            #2.设置命令返回值：一般只包含一行，这一行值为OK字符串。
            #3.发送数据命令返回值：一般返回一行，且为提示符>
            #4.命令执行错误返回值：一般为只有一行，且以+CME ERROR:开头
            #5.还有其他类型，关于他们的判断可以在相应的代码里面直接进行添加。

            #经过对上面的返回响应进行详细的分析，以及结合程序执行的效率和逻辑性，可以对上面的情况
            #进行一一的判断，并制定好相应的判断顺序。将返回响应从字节少到多的顺序进行检查。
            #那么这里最先得到排查的就是响应是不是数据输入提示符。
            #如果是数据输入提示符，那么也就意味着不会再接收到其他响应了，这样就可以直接结束读取操作了。
            #之前自己写的程序就没有考虑到这些问题，导致其实自己并不知道是否已经将数据读取完毕，当时也没有
            #设置读取多长时间就将程序结束，如果没有时间设置，当命令执行之后没有响应时，就会导致程序一直
            #停在那里，不在继续执行其他语句，所以这里的代码是非常严谨的，时长设置是大范围设置，可以排除
            #没有响应返回的干扰，每次读取一个字节，可以顺便对返回响应类型进行判断，最终判断是否读取完毕，
            #标准就是是否出现一行OK字符串，或者其他与OK同等级别代表响应结束的字符串，例如+CME ERROR字符串。

            #raw指生的未加工的，这里之所有这样命名是说明从串口中读出原始数据
            #原始数据主要是以字节进行编码
            #这里之所以先读一个字节，因为如果刚执行的命令是准备发送数据，如短信，
            #TCP通信，那么响应就是一个字节的提示符
            #创建串口对象时timeout参数是0.5秒，因此read函数会等待0.5秒读取串口缓冲区1字节的值并返回
            raw = self.serial.read(1)
            if len(raw) == 0:
                continue

            #参数:ignore，忽略非法字符
            #将从串口得到的原生数据进行解码，并忽略非法字符
            rawdata = raw.decode(self.coding, 'ignore')
            if rawdata == '>':
                atLogger.get_resp(rawdata)
                return True

            #将读取的每一字节值都依次放到字节数组里面
            self.inparsing.extend(raw)
            size = len(self.inparsing)

            if len(self.inparsing) < 2:
                continue

            #当self.inparsing数组里面的值等于两个或者超过两个字节的时候就要对其最后两个字节进行判断
            #如果是ord('\r')和ord('\n')，那么就代表已经读到了一行响应，这时候就可以将其打印出来，
            #并将self.inparsing清空，一遍进行下一行数据的处理
            #接下来还要对这一行进行响应末尾判断，一遍确认是否对响应处理完毕，如果这一行是OK，+CME ERROR:开头
            #等，那么整个读取就过程就结束了，所以，并不是自己刚开始写代码时的把所有响应读出来进行判断。
            if self.inparsing[-2] == ord('\r') and self.inparsing[-1] == ord('\n'):
                #将每行的空格等空白符删除
                line = self.inparsing.decode(self.coding, 'ignore').strip()
                #self.inparsing存储的一行响应，一旦一行结束就将这行打印出来，将自身清空
                #存储下一行数据
                self.inparsing.clear()
                atLogger.get_resp(line)
                #对所有响应进行保存，将响应以列表形式进行保存，这个跟自己刚开始写的程序处理方法相同。
                self.resp.append(line)
                if expected(line):
                    return True

    #这个函数的返回值始终为True，
    def send(self, cmd, timeout):
        """ Send an AT commmand, read responses till either OK or ERROR
            * \r\n will be appended to command automatically
            * the command is save for later checking
            * all responses are saved for later checking

            NOTE: even ERROR is read, this function will return True
        """
        global atLogger
        if not self.serial:
            raise Exception("!!! Serial port isn't open")

        atLogger.send_cmd(cmd)
        self.last_cmd = cmd.strip()
        self.resp.clear()

        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()
        self.serial.write((cmd + "\r\n").encode())
        return self.__read_resp(timeout, AtChat.__check_ok_error)

    def wait(self, line, timeout):
        """ Read responses till the specified line
            All responses are saved for later checking
        """
        if not self.serial:
            raise Exception("!!! Serial port isn't open")

        AtChat.line_checked = line
        self.resp.clear()
        return self.__read_resp(timeout, AtChat.__check_line)

    def send_ok(self, cmd, timeout):
        """ Send an AT commmand, and check response OK """
        return self.send(cmd, timeout) and self.has(self.OK)

    #此函数返回值是True，代表响应读取完毕
    #至于响应是否符合期望，还需要进一步对响应值进行判断
    #因为此函数已经将响应值存储到了类的全局变量当中，可以直接供其他函数对
    #响应值进行判断，返回值为False，则读取响应失败

    def get_uptime(self):
        """ Get module up time by AT command, and return -1 on fail
        """
        if not atChat.send_ok("AT+UPTIME", 1.0):
            return -1.0

        line = atChat.get_line_starts("^UPTIME:")
        if line is None:
            return -1.0
        return int(line.split()[1]) / 1000.0

    def get_csq(self):
        """ Get CSQ by AT command, and return -1 on fail
        """
        if not atChat.send_ok("AT+CSQ", 1.0):
            return -1

        line = atChat.get_line_starts("+CSQ:")
        if line is None:
            return -1
        return int(line.split()[1].split(',')[0])


""" Global object """
atChat = AtChat()

class RelayControl(object):
    """ Open/close relay channel through socket """

    def __init__(self):
        self.host = atConfig.relay_server
        self.port = atConfig.relay_port
        self.bufsize = 1024
        self.addr = (self.host, self.port)

    def __conn_host(self, masg):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(self.addr)
        client.send(masg.strip().encode())
        data = client.recv(self.bufsize).decode()
        if 'OK' not in data:
            client.close()
            raise Exception("Error when %s" % masg)
        client.close()

    def open_channel(self, index=atConfig.relay_channel):
        self.__conn_host('open %d' % index)

    def close_channel(self, index=atConfig.relay_channel):
        self.__conn_host('close %d' % index)


""" Global object"""
relayCtrl = RelayControl()

class PppControl(object):
    """ Dial/hangup PPP """

    def __init__(self):
        pass

    def dialup(self, entryname):
        res = {'reValue': False, 'msg': ''}
        try:
            dp,b = win32ras.GetEntryDialParams(None, entryname)
        except:
            raise Exception("Couldn't find DUN entry: %s" % entryname)
        else:
            pid,ret = win32ras.Dial(None, None, (entryname, "", "", dp[ 3 ], dp[ 4 ], ""), None)
            if ret == 0:
                res['reValue'] = True
                res['msg'] = 'PPP Dial up Success!'
            else:
                res['msg'] = 'PPP Dial Fail: %s' % win32ras.GetErrorString(ret)
                res['reValue'] = False
                
        return res

    def disconnect(self, rasEntry):
        name = rasEntry.lower()
        for hcon, entryName, devName, devType in win32ras.EnumConnections():
            if entryName.lower() == name:
                try:
                    win32ras.HangUp(hcon)
                except:
                    raise Exception("Error when hangup %s!" % name)
                break
        else:
            raise Exception("Could not find an open connection to %s" % name)


""" Global object """
pppCtrl = PppControl()

class SocketControl(object):
    """ Connect/disconnect to host or send data to host """

    def __init__(self):
        self.client = None
  
    def connect_host(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        res = self.client.connect_ex((atConfig.echo_server, int(atConfig.echo_port)))
        return res

    def send_data(self, data):
        res = self.client.send(data.strip().encode())
        atLogger.send_cmd(data)
        return res

    def recv_data(self, recvlen, timeout):
        recvdata = ''
        starttime = time.time()
        while True:
            if  time.time() >= starttime + timeout:
                return recvdata
            res = self.client.recv(recvlen).decode().strip()
            if not len(res) == 0:
                atLogger.get_resp(res)
            recvdata += res
            if len(recvdata) >= recvlen:
                return recvdata
    
    def disconnect_host(self):
        if self.client != None:
            self.client.close()
            self.client = None


""" Global object """
sockCtrl = SocketControl()

class netControl(object):
    """modify route and net config """

    def __init__(self):
        pass

    def find_ip(self):
        match_ip = ''
        ipconfig_ls = os.popen('ipconfig /all').readlines()
        for i in range(0, len(ipconfig_ls)):
            if re.search(r'PPP', ipconfig_ls[i]) != None and\
                re.search(atConfig.entry_name, ipconfig_ls[i]) != None:
                for j in range(1, 10):
                    if re.search(r'IPv4', ipconfig_ls[i+j]) != None:
                        match_ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ipconfig_ls[i+j]).group(0)
        return match_ip

    def set_route(self, bindAddr):
        ppp_ip = self.find_ip()
        if ppp_ip == '':
            atLogger.case_log('Cannot find ppp connect')
            return False
        p = subprocess.Popen('route delete 0.0.0.0', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        out = p.stdout.read().decode('gb2312')
        if '操作完成' not in out:
            atLogger.case_log(out)
            atLogger.case_log('Fail to delete route 0.0.0.0')
            return False
        p = subprocess.Popen('route add 0.0.0.0 mask 0.0.0.0 %s' % atConfig.local_conn_addr, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        out = p.stdout.read().decode('gb2312')
        if '操作完成' not in out:
            atLogger.case_log(out)
            atLogger.case_log('Fail to add route 0.0.0.0')
            return False
        p = subprocess.Popen('route add %s mask 255.255.255.255 %s' % (bindAddr,ppp_ip), stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        out = p.stdout.read().decode('gb2312')
        if '操作完成' not in out:
            atLogger.case_log(out)
            atLogger.case_log('Fail to add route ' + atConfig.echo_server)
            return False
        return True
    
    def reset_localconn(self):
        p = subprocess.Popen('netsh interface set interface name="本地连接" admin=DISABLED', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode('gb2312')
        atLogger.case_log(out)
        if len(out) > 2:
            atLogger.case_log('Fail to disable local connect')
            return False
        p = subprocess.Popen('netsh interface set interface name="本地连接" admin=ENABLED', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode('gb2312')
        atLogger.case_log(out)
        if len(out) > 2:
            atLogger.case_log('Fail to enable local connect')
            return False
        return True

""" Global object """
netCtrl = netControl()
        