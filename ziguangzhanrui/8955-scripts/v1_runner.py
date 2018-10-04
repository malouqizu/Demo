from comm.atconfig import atConfig
from comm.atlogger import atLogger

if __name__=="__main__":
    print(atConfig.com_port)
    atLogger.case_start("AT")
    atLogger.command_send("AT")
    atLogger.get_res("OK")
    atLogger.case_end("AT")
