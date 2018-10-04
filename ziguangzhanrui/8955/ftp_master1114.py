#!/usr/bin/env python
import os
import time
import sys
import random
import serial
import getopt
import re

FTPSerial = '/dev/ttyUSB1'

APN = 'CMNET'
FTPServer = '"111.205.140.137:11009"'
USER_UP = '"upload"'
USER_DOWN = '"download"'
PASSWORD = '"123456"'
FTPMODE = '1'
FTPTOUT = '180'
FTPTYPE = '0'

default_up_path = '/'
mode = ''
trans_file = ''
local = ''
uploadsize = 1024 * 256
write_once = 1440
read_once = 1024

def parseParam(argv):
    global mode, local, APN,FTPServer,FTPSerial,trans_file
    opts, args = getopt.getopt(sys.argv[1:], "hs:m:a:u:f:l:")
    for op, value in opts:
        if op == "-a":
            APN = value
        elif op == "-s":
            FTPSerial = value
        elif op == "-u":
            FTPServer = value
        elif op == "-f":
            trans_file = value
        elif op == "-m":
            mode = value
        elif op == "-l":
            local = value
        elif op == "-h":
            usage()
            sys.exit()

def usage():
    print("usage:\n\
            -m <down/up> -- upload test or download test\n\
            -s <serial>  -- (/dev/ttyUSB0) modem device\n\
            -u <url>     -- server url\n\
            -f <file>    -- up/download file path\n\
            -l <file>    -- local file path to put to server\n\
            -a <apn>     -- (CMNET) maybe CMNET, UNINET ...\n")

def ATCommand(cmd):
    global ser
    cmd = cmd + '\r\n'
    ser.write(cmd)
    print(cmd)

def ftpclose():
    ATCommand('AT^FTPCLOSE')
    ATWaitRsp('OK')

def ATWaitRsp(match):
    while(True):
        line = ser.readline()
        print('%s' % line)
        if (re.search(match, line)):
            break
    return line

def NetworkConfig():
    global ser
    global FTPSerial
    global APN

    #showconfig()
    ser = serial.Serial(FTPSerial, 115200, rtscts=False, xonxoff=False, dsrdtr=False, timeout=60)
    ATCommand('ATE0')
    ATWaitRsp('OK')
    ATCommand('AT+CGDCONT=1,"IP","' + APN + '",')
    ATWaitRsp('OK')
    ATCommand('AT+CGATT=1')
    ATWaitRsp('OK')
    ATCommand('AT+CGACT=1,1')
    ATWaitRsp('OK')

def FTPOpen(server, user, passwd):
    ATCommand('AT^FTPOPEN=' + server + ',' + user + ',' + passwd + ',' \
            + FTPMODE + ',' + FTPTOUT + ',' + FTPTYPE + '')
    ATWaitRsp('OK')

def random_str(len):
    str=""
    for i in range(len):
        str+=(random.choice(" ABCDEF "))
    return str

def FTPDownload(file):
    SaveFile = file.split('/')[-1]
    if os.path.exists(SaveFile):
        os.remove(SaveFile)

    save = open(SaveFile, 'w')

    NetworkConfig()
    FTPOpen(FTPServer, USER_DOWN, PASSWORD)
    ATCommand('AT^FTPGETSET="' + file + '"')
    ATWaitRsp('OK')

    ATCommand('AT^FTPGET=1')
    ATWaitRsp('OK')
    ATWaitRsp('FTPGET:1,1')

    data_len = 0
    total = 0
    time_start = time.time()
    while True:
        line = ATWaitRsp('FTPGET:')
        spline = line.split(',')
        if len(spline) == 2:
            get_len = int(line.split(',')[1])
            if (get_len == 0):
                print(' download finish!!')
                break
        data = ser.read(get_len)
        data_len = len(data)
        save.write(data)
        total += data_len
        print('get = %d , total=%d' % (data_len, total))

    time_end = time.time()
    print('spent time %s s, sent %d bytes, speed = %d byte/s' %(time_end - time_start, total, total/(time_end - time_start)))
    save.close()
    ftpclose()

def FTPUpload(file, size):
    NetworkConfig()
    FTPOpen(FTPServer, USER_UP, PASSWORD)
    ATCommand('AT^FTPPUTSET="' + file + '"')
    ATWaitRsp('OK')

    ATCommand('AT^FTPPUT=1')
    ATWaitRsp('OK')
    while True:
        line = ATWaitRsp('FTPPUT')
        if ('^FTPPUT:1' in  line):
            spline = line.split(',')
            if len(spline) == 2:
                maxlength = int(line.split(',')[1])
                print('maxlength = %d' % maxlength)
                break
            else:
                print('get error')
                no_error = False
                return

    time_start = time.time()
    sended = 0
    while(size > 0):
        if (size <= maxlength):
           maxlength = size
        ATCommand('AT^FTPPUT=2,' + str(maxlength) + ' ')
        ser.write(random_str(maxlength))
        ATWaitRsp('OK')
        size -= maxlength
        sended += maxlength
        print('left=%d, send size=%d ,sended=%d' % (size , maxlength, sended))

    time_end = time.time()
    print('spent time %s s, sent %d bytes, speed = %d byte/s' %(time_end - time_start, sended, sended/(time_end - time_start)))
    ATCommand('AT^FTPPUT=2,0')
    ATWaitRsp('OK')
    ATWaitRsp('\^FTPPUT:2,0')
    ftpclose()

def SerialWrite(data, len):
    left = len
    offset = 0
    while left > 0:
        w = ser.write(data[offset:])
        offset += w
        left -= w
        if left > 0:
            print('=========len=%d, w=%d,writed=%d, left=%d' % (len, w,offset, left))

def FTPUploadFile(InputFile, Path):
    if os.path.exists(InputFile):
        input = open(InputFile, 'r')
    else:
        print(InputFile + ' is not exists')
        return

    NetworkConfig()
    FTPOpen(FTPServer, USER_UP, PASSWORD)
    ATCommand('AT^FTPPUTSET="' + Path + '"')
    ATWaitRsp('OK')

    ATCommand('AT^FTPPUT=1')
    ATWaitRsp('OK')
    while True:
        line = ATWaitRsp('FTPPUT')
        if ('^FTPPUT:1' in  line):
            spline = line.split(',')
            if len(spline) == 2:
                maxlength = int(line.split(',')[1])
                print('maxlength = %d' % maxlength)
                break
            else:
                print('get error')
                no_error = False
                return

    time_start = time.time()
    sended = 0
    while True:
        data = input.read(maxlength)
        if (data == ''):
            break

        read_len = len(data)
        ATCommand('AT^FTPPUT=2,' + str(read_len) + ' ')
        SerialWrite(data, read_len)
        rsp = ATWaitRsp('OK|ERROR')
        if 'ERROR' in rsp:
            print('get error exit')
            exit()
        sended += read_len
        print('left=%d, send size=%d ,sended=%d' % (read_len, maxlength, sended))

    time_end = time.time()
    print('spent time %s s, sent %d bytes, speed = %d byte/s' %(time_end - time_start, sended, sended/(time_end - time_start)))
    input.close()
    ATCommand('AT^FTPPUT=2,0')
    ATWaitRsp('OK')
    ATWaitRsp('\^FTPPUT:2,0')
    ftpclose()

if __name__ == "__main__":
    parseParam(sys.argv[1:])
    if mode == 'up':
        if trans_file == '':
            FTPUploadFile(local, default_up_path + local.split('/')[-1])
            exit()
        else:
            FTPUploadFile(local, trans_file)
    elif mode == 'down':
        FTPDownload(trans_file)
    else:
        usage()


