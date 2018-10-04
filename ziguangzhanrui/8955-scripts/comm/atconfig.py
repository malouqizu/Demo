import os
import time

COMPORT="COM4"

class AtConfig(object):
    def __init__(self):
        self.log_file=os.environ.get("AT_TEST_LOG_FILE","log.txt")
        self.com_port=COMPORT

atConfig=AtConfig()

if __name__=="__main__":
    print("我是模块atconfig!")
    print(atConfig.log_file)
    print(atConfig.com_port)
