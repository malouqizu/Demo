import sys
import datetime
from comm.atconfig import atConfig

class AtLogger(object):
    def __init__(self):
        self.fh=None
        if self.fh is None:
            try:
                self.fh=open(atConfig.log_file,'w')
            except:
                self.fh=None

    def __del__(self):
        if self.fh is not None:
            self.fh.close()

    def __write(self,logstr):
        if self.fh is not None:
            self.fh.write(logstr)
            self.fh.flush()
        else:
            sys.stdout.write(logstr)

    def log_timed(self,logstr):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]%s\n" % (stamp, logstr))

    def case_start(self,case):
        stamp=datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]====== case: %s [start] ======\n" %(stamp,case))

    def case_end(self,case):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]====== case: %s [end] ======\n\n" % (stamp, case))

    def command_send(self,command):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]Sen: %s\n" % (stamp, command))

    def get_res(self,res):
        stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.__write("[%s]Rec: %s\n" % (stamp, res))

atLogger=AtLogger()

if __name__=="__main__":
    print("我是模块：atlogger!")
    atLogger.case_start("AT")
    atLogger.command_send("AT")
    atLogger.get_res("ok")
    atLogger.case_end("AT")
