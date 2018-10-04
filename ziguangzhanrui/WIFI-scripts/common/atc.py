import os
import time
import datetime
import sys
import serial

COMPORT="COM39"
BAUDRATE=921600

class AtConfig(object):
    def __init__(self):
        self.log_file_name=os.environ.get("AT_TEST_LOG_FILE","log.txt")
        self.com_port=COMPORT

#global object
atConfig=AtConfig()

class AtLogger(object):
    def __init__(self):
        self.fh=None
        if self.fh == None:
            try:
                self.fh=open(atConfig.log_file_name,'w')
            except:
                self.fh=None
        self.start_time=time.time()

    def __write(self,out):
        if self.fh is not None:
            self.fh.write(out)
            self.fh.flush()
        sys.stdout.write(out)

    def case_log(self,line):
        self.__write("%s\n" % (line.strip()))

    def case_start(self,name):
        self.__write("====== %s [start] ======\n" %(name.strip()))

    def case_end(self,name):
        self.__write("====== %s [end] ======\n" %(name.strip()))

    def send_cmd(self,line):
        stamp=datetime.datetime.now().strftime("%H%M%S.%f")[-3]
        self.__write("[%s]>>> %s\n"%(stamp,line.strip()))

    def get_rsp(self,line):
        stamp = datetime.datetime.now().strftime("%H%M%S.%f")[-3]
        self.__write("[%s]<<< %s\n" % (stamp, line.strip()))

    def case_timed_log(self, line):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]--- %s\n" % (stamp, line.strip()))

    def __del__(self):
        if self.fh is not None:
            self.fh.close()

#global object
atLogger=AtLogger()

#关于类AtChat的编写，要思考的内容
#首先要考虑这个类模型的主要作用是什么？
#只有考虑清楚了这个类的作用，才能正确的
#构造这个类，那么这里类的主要作用是：
#与串口进行通信，给串口发送命令让模块执行
#通过串口接收的命令，命令被执行之后，执行
#命令的函数会返回相应的响应，这个响应会传送给
#串口，那么就可以读取响应，进一步对响应进行判断
#看是否符合期望值
#因此，这个类要实现的核心功能有三个：
#给串口发送命令
#1.打开串口
#1.1设置串口需要的参数
#1.2导入处理串口的模块
#1.3创建串口对象，打开串口
#2.发送命令
#2.1对命令进行格式处理
#2.2发送命令
#从串口读取执行命令后输出的响应
#3.读取响应
#3.1读出响应
#3.2对响应进行处理，转换成适合进行判断的方式
#对输出的响应进行判断
#4.判断响应
#响应有好几种，因此要根据响应的内容格式，来进行相应的
#判断，那么针对判断函数就应该有好几个
#4.1判断响应值是否与期待的响应值相同。
#4.2判断响应值是否含有某个字符串。
#4.2.1判断响应值是否含有OK字符串。
#4.2.2判断响应值是否含有ERROR字符串。
#4.2.3判断响应值是否含有ECHO字符串。
#5.关闭串口

class AtChat(object):
    def __init__(self):
        self.port=atConfig.com_port
        self.baudrate=115200
        self.bytesize = serial.EIGHTBITS
        self.parity=serial.PARITY_NONE
        self.stopbits=serial.STOPBITS_ONE
        self.timeout = 0.5
        self.xonxoff=False
        self.rtscts=False
        self.write_timeout = 1.0
        self.dsrdtr=False

    def com_open(self):
        if self.ser is not None:
            return
        self.ser=serial.Serial(self.port,
                               self.baudrate,
                               self.bytesize,
                               self.parity,
                               self.stopbits,
                               self.timeout,
                               self.xonxoff,
                               self.rtscts,
                               self.write_timeout,
                               self.dsrdtr)
    def com_close(self):
        if self.ser is not None:
            self.ser.close()
        else:
            return

    def com_reopen(self):
        if self.ser is not None:
            self.ser.close()
        self.ser.open()

    def send(self,cmd,timeWaiting,check):
        global atLogger

        #判断串口是否已经被打开
        if self.ser == None or self.ser.closed:
            raise Exception("Serial port not open!!!")

        #发送需要执行的命令
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write((cmd+"\r\n").encode())

        #获得刚才执行命令的响应
        time.sleep(timeWaiting)
        for i in range(0,100):
            self.rsize=self.ser.in_waiting
            if self.rsize>0:
                self.rcontext=self.ser.read(self.rsize).decode()
                #self.rcontext = self.ser.read(self.rsize).decode('utf-8').strip()
                self.rcontext=self.rcontext.split("\r\n")
            time.sleep(0.1)
        else:
            #print("没有从串口读取到任何内容！")
            self.rcontext=None

        #对命令的响应进行判断
        #1.响应是否包含特定的字符串
        #2.响应是否是按期望的顺序出现
        #3.得到以固定字符串为首的部分响应


    def read_res(self,timeWaiting):
        time.sleep(timeWaiting)
        for i in range(0,100):
            self.rsize=self.ser.in_waiting
            if self.rsize>0:
                self.rcontext=self.ser.read(self.rsize).decode()
                #self.rcontext = self.ser.read(self.rsize).decode('utf-8').strip()
                self.rcontext=self.rcontext.split("\r\n")
                return  self.rcontext
            time.sleep(0.1)
        else:
            #print("没有从串口读取到任何内容！")
            return None


class Com():
    def __init__(self,port,baudrate,timeout=None):
        #串口号
        self.port=port
        #串口波特率
        self.baudrate=baudrate
        #读时延
        self.timeout=timeout

    def com_open(self):
        try:
            import serial
        except ImportError:
            raise Exception('Not able to find PySerial installation or may be is not installed.')

        self.ser=serial.Serial(self.port,self.baudrate,timeout=self.timeout)
        #return self.ser

    def com_write(self,context):
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        self.wcontext=(context+"\n").encode('utf-8')
        self.wsize=self.ser.write(self.wcontext)
        #print("通过串口发送",self.wsize,"字节")
        return self.wsize

    #将读到的响应用以\r\n为分隔符存储成列表
    def com_read(self):
        while True:
            self.rsize=self.ser.in_waiting
            if self.rsize>0:
                self.rcontext=self.ser.read(self.rsize).decode('gbk').strip()
                #self.rcontext = self.ser.read(self.rsize).decode('utf-8').strip()
                self.rcontext=self.rcontext.split("\r\n")
                return  self.rcontext
            time.sleep(0.1)
        else:
            print("没有从串口读取到任何内容！")
            return None

    def com_close(self):
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        self.ser.close()

class Attest():
    def __init__(self):
        self.com=Com(COMPORT,BAUDRATE)
        self.com.com_open()

    #将期望的响应用列表进行存储
    def executeCmd(self,cmd):
        self.com.com_write(cmd)
        self.response=self.com.com_read()
        return self.response

    def attest_close(self):
        self.com.com_close()

