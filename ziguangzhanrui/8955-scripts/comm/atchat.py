import serial
import time
import sys

from comm.atconfig import atConfig
from comm.atlogger import atLogger

class AtChat(object):
    def __init__(self):
        self.port = atConfig.com_port
        self.baudrate = 115200
        self.bytesize = serial.EIGHTBITS
        self.parity = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE
        self.timeout = 2
        self.xonxoff = False
        self.rtscts = False
        self.write_timeout = 1.0
        self.dsrdtr = False

        self.coding='utf-8'
        self.ser=None
        self.inparsing=bytearray()
        self.res=list()

        self.line_checked=''
        self.line_checked_contained=''

        #atLogger.log_timed(self.port)
        #sys.stdout.write(str(self.port))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.baudrate)
        #sys.stdout.write(str(self.baudrate))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.bytesize)
        #sys.stdout.write(str(self.bytesize))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.parity)
        #sys.stdout.write(str(self.parity))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.stopbits)
        #sys.stdout.write(str(self.stopbits))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.timeout)
        #sys.stdout.write(str(self.timeout))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.xonxoff)
        #sys.stdout.write(str(self.xonxoff))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.rtscts)
        #sys.stdout.write(str(self.rtscts))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.write_timeout)
        #sys.stdout.write(str(self.write_timeout))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.dsrdtr)
        #sys.stdout.write(str(self.dsrdtr))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.coding)
        #sys.stdout.write(str(self.coding))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.ser)
        #sys.stdout.write(str(self.ser))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.inparsing)
        #sys.stdout.write(str(self.inparsing))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.res)
        #sys.stdout.write(str(self.res))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.line_checked)
        #sys.stdout.write(str(self.line_checked))
        #sys.stdout.write("\r\n")

        #atLogger.log_timed(self.line_checked_contained)
        #sys.stdout.write(str(self.line_checked_contained))
        #sys.stdout.write("\r\n")

    def com_open(self):
        if self.ser is not None:
            return

        self.ser=serial.Serial(port=self.port,
                               baudrate=self.baudrate,
                               bytesize=self.bytesize,
                               parity=self.parity,
                               stopbits=self.stopbits,
                               timeout=self.timeout,
                               xonxoff=self.xonxoff,
                               rtscts=self.rtscts,
                               write_timeout=self.write_timeout,
                               dsrdtr=self.dsrdtr)
        atLogger.log_timed("%s opened!" % self.ser.name)
        sys.stdout.write("%s opened!" % self.ser.name)
        sys.stdout.write("\r\n")


    def com_close(self):
        self.ser.close()
        atLogger.log_timed("%s closed!" % self.ser.name)
        sys.stdout.write("%s closed!" % self.ser.name)
        sys.stdout.write("\r\n")
        self.ser=None

    def com_reopen(self):
        if self.ser is not None:
            self.ser.close()
            atLogger.log_timed("%s closed!" % self.ser.name)
            sys.stdout.write("%s closed!" % self.ser.name)
            sys.stdout.write("\r\n")
        self.ser.open()
        atLogger.log_timed("%s reopened!" % self.ser.name)
        sys.stdout.write("%s reopened!" % self.ser.name)
        sys.stdout.write("\r\n")

    #发送命令，并得到命令执行后的响应结果
    #函数执行成功的终极目的是判断是否出现OK，+CME ERROR:，>，CLOSE OK，SEND OK
    def send_command(self,command,timeWaitting=1):
        if self.ser is None or self.ser.closed:
            raise Exception("com is not open！！！")

        global atLogger
        atLogger.command_send(command)

        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write((command+'\r\n').encode())

        # return self.read_response(timeWaitting,AtChat.check_ok_error)
        self.res.clear()

        if timeWaitting is not None:
            self.endtime = time.time() + timeWaitting

        while True:
            if timeWaitting is not None and time.time()>self.endtime:
                print("超时！")
                return False

            raw=self.ser.read(1)
            if len(raw)<1:
                continue

            rawdata=raw.decode(self.coding, 'ignore')
            if rawdata==">":
                atLogger.get_res(rawdata)
                print(rawdata)
                print("读取一个字符，且该字符提示要输入数据！")
                return True

            self.inparsing.extend(raw)
            size=len(self.inparsing)

            if size<2:
                continue

            if self.inparsing[-2]==ord("\r") and self.inparsing[-1]==ord("\n"):
                line=self.inparsing.decode(self.coding, 'ignore').strip()
                self.inparsing.clear()
                atLogger.get_res(line)
                self.res.append(line)
                print(line)
                if "OK" == line or line.startswith("+CME ERROR:") or line.startswith(">") or \
                        line.startswith("CLOSE OK") or line.startswith("SEND OK"):
                    print("响应符合要求，读取结束!")
                    return True

    def has(self,line):
        if len(self.res)>0:
            for r in self.res:
                if r == line.upper():
                    return True
            else:
                return False
        else:
            atLogger.log_timed("no response!!!")
            return False

    def has_in_order(self,expected):
        self.res.pop(0)
        for r in self.res:
            if r=='':
                self.res.remove(r)

        for r in self.res:
            print(r)

        for e in expected:
            if e=='':
                expected.remove(e)
        for e in expected:
            print(e)

        cnt=0
        if len(expected)==len(self.res):
            for m,n in zip(expected,self.res):
                if m.upper()==n:
                    cnt=cnt+1
            if cnt==len(expected):
                return True
            else:
                return False


atChat=AtChat()

if __name__=="__main__":
    atChat.com_open()

    atLogger.case_start('at')
    atChat.send_command('at')
    time.sleep(10)
    atLogger.case_end('at')
    atLogger.log_timed("\n")

    atLogger.case_start('at+hello')
    atChat.send_command('at+hello')
    time.sleep(10)
    atLogger.case_end('at+hello')
    atLogger.log_timed("\n")

    atLogger.case_start('atd15011552375')
    atChat.send_command('atd15011552375')
    time.sleep(10)
    atLogger.case_end('atd15011552375')
    atLogger.log_timed("\n")

    atLogger.case_start('ath')
    atChat.send_command('ath')
    time.sleep(10)
    atLogger.case_end('ath')
    atLogger.log_timed("\n")

    atChat.com_close()









