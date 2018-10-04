#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__date__ = '10 Feb, 2017'
__author__ = 'jinxie@rdamicro.com'

import sys
import time

COMPORT = 'COM4'

class AtCommand(object):

    def __init__(self, port):
        self.comport = port
        self.timeout = 3
        self.com = None
        self.data = None
        self.atcommand = None

    def __enter__(self):
        self.open(self.comport, self.timeout)
        return self

    def __exit__(self, typeof, value, tbx):
        self.close()
    
    # Connect to the specified AT COM Port with a required Timeout
    def open(self, port, timeout=10):
        self.comport = port
        self.timeout = timeout
        try:
            import serial
        except ImportError:
            raise Exception('Not able to find PySerial installation or may be is not installed.')

        self.com = serial.Serial(self.comport, 115200, timeout=10)

    # Send an AT Command, store output data and response in a tuple and return it
    def send(self, atcommand, TIMEWAITING=.3, resp=True):
        self.com.flushInput()
        self.com.flushOutput()
        
        self.atcommand = atcommand
        self.com.write((self.atcommand + "\r\n").encode())
        if resp:
            time.sleep(TIMEWAITING)
            return self.read()
        else:
            return None

    # Read the output data and response from DUT
    def read(self):
        for _ in range(10):  # try 10 times in 1s interval
            size = self.com.inWaiting()
            if size > 0:
                break
            time.sleep(1)
        else:
            return (self.atcommand.strip(), None)
        raw = self.com.read(size).decode('utf-8')
        self.data = list(l for l in raw.split('\r\n') if l.strip())
        if self.data[0].upper().startswith("AT"):
            return (self.data[0].strip(), self.data[1:])
        else:
            return (self.atcommand, self.data)

    # Clear the Input and Output buffer, and close the serial connection.
    def close(self):
        self.com.flushInput()
        self.com.flushOutput()
        self.com.close()

class AtTest(object):
	
    def __init__(self, port):
        self.port = port

    def __enter__(self):
        return self

    def __exit__(self, typeof, value, tbc):
        pass

    # Send AT command to DUT
    def to(self, cmd, TIMESLEEP=.3, resp=True):
        with AtCommand(self.port) as atc:
            cmd.encode()
            return atc.send(cmd, TIMESLEEP, resp)
    
    # Execute cmd and verify its response 
    def executeCmd(self, cmd, TIMEOUT=.3, *expctedCmdBuf):
        cmdResp = self.to(cmd, TIMEOUT)
        nCmdRespList = len(cmdResp[1])
        if cmdResp[1][nCmdRespList - 1] == "OK":
            print('>>> ')
            print('>>> AT cmd sent : ' + cmd)
            i = 0
            for buf in expctedCmdBuf:
                if buf == cmdResp[1][i]:
                    print('>>> Unsolicited : ' + buf)
                    i += 1
                else:
                    print('>>> Actual unsolicited  : ' + cmdResp[1][i])
                    print('>>> Expected unsolicted : ' + buf)
                    raise Exception('!!! Incorrect unsolicited code !!!');
            print('>>> AT cmd resp : ' + cmdResp[1][nCmdRespList - 1])
            return True

        print('>>> AT cmd resp : ' + cmdResp[1][nCmdRespList - 1])
        raise Exception('!!! Failed to execute the test case !!!')

if __name__ == '__main__':
    pass
