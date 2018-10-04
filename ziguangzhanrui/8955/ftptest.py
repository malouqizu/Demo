#!/usr/bin/env python 
import time
import sys
import random
import serial
import getopt

apn = 'CMNET'
mode = ''
port = '/dev/ttyUSB1'
downloadfile = '/file.1M'
putfile = '/upload.txt'

url = "111.205.140.137:11009"
upuser = 'upload'
downuser = 'download'
passwd = '123456'
ftpmode = '1'
ftpTout = '180'
ftptype = '0'

uploadsize = 1024 * 1024
write_once = 1440
read_once = 1024

def ftpcmd(cmd):
    global ser
    ser.write(cmd)
    print(cmd)

def waitrsp(rsp):
    while(True):
        line = ser.readline()
        print('%s' % line)
        if (rsp in line):
            break
    return line
    
def ftpclose():
    ftpcmd('AT^FTPCLOSE\r\n')
    waitrsp('OK')

def ftpprepare():
    global ser
    global port

    showconfig()
    ser=serial.Serial(port, 115200, rtscts=False, timeout=60)
    ftpcmd('ATE0\r\n')
    waitrsp('OK')
    cmd = 'AT+CGDCONT=1,"IP","' + apn + '",\r\n'
    ftpcmd(cmd)
    waitrsp('OK')
    ftpcmd('AT+CGATT=1\r\n')
    waitrsp('OK')
    ftpcmd('AT+CGACT=1,1\r\n')
    waitrsp('OK')

def random_str(len):  
    str=""  
    for i in range(len):  
        str+=(random.choice(" ABCDEF "))  
    return str 

def uploadtest(len):
    print('send total file size=%d' % len)
    open_cmd = 'AT^FTPOPEN=' + url + ',' + upuser + ',' + passwd + ',' \
            + ftpmode + ',' + ftpTout + ',' + ftptype + '\r\n'
    ftpcmd(open_cmd)
    waitrsp('OK')
    left = len
    sended = 0
    count = 0
    while left > 0:
        if left < write_once:
            s = left
        else:
            s = write_once

        left = left - s
        if left == 0:
            cmd = 'AT^FTPPUT=' + putfile + ',' + str(s) +',' + '1\r\n'
        else:
            cmd = 'AT^FTPPUT=' + putfile + ',' + str(s) +',' + '0\r\n'
        ftpcmd(cmd)
        waitrsp('CONNECT')
        if count == 0:
            time_start = time.time()

        ser.write(random_str(s))
        waitrsp('OK')
        sended += s
        print('left=%d, send size=%d ,sended=%d' % (left, s, sended))
        count+=1

    waitrsp('URCFTP:1')
    time_end = time.time()

    print('spend time %s s, sended %d bytes, speed = %d byte/s' %(time_end - time_start, len, len/(time_end - time_start)))
    ftpclose()

def downloadtest(file):
    open_cmd = 'AT^FTPOPEN=' + url + ',' + downuser + ',' + passwd + ',' \
            + ftpmode + ',' + ftpTout + ',' + ftptype + '\r\n'
    ftpcmd(open_cmd)
    waitrsp('OK')
    cmd = 'AT^FTPSIZE="' + file + '"\r\n'
    ftpcmd(cmd)
    line=waitrsp('FTPSIZE')
    filesize = int((line[len('^FTPSIZE:'):]))
    print(file + ' size=%d' % filesize)
    waitrsp('OK')

    left = filesize
    cmd = 'AT^FTPGET="' + file + '"\r\n'
    ftpcmd(cmd)
    waitrsp('CONNECT')
    time_start = time.time()
    while left > 0:
        if left > read_once:
            readsize = read_once
        else:
            readsize = left

        rlen = len(ser.read(readsize))
        left -= rlen
        print('readed:%d, left=%d' % (rlen, left))

    waitrsp('OK')
    waitrsp('URCFTP:1')
    time_end = time.time()
    print('spend time %d s, receive %d bytes, speed = %d byte/s' %(time_end - time_start, filesize, filesize/(time_end - time_start)))
    ftpclose()

def showconfig():
    print('url:' + url)
    print('mode:' + mode)
    print('serial:' + port)
    print('downuser:' + downuser)
    print('upuser:' + upuser)
    print('passwd:' + passwd)
    print('downloadfile:' + downloadfile)
    print('uploadsize:%d' % uploadsize)

def parseParam(argv):
    global port
    global apn 
    global mode
    global downloadfile
    
    opts, args = getopt.getopt(sys.argv[1:], "hs:m:a:u:f:")
    for op, value in opts:
        if op == "-a":
            apn = value
        elif op == "-s":
            port = value
        elif op == "-u":
            url = value
        elif op == "-f":
            downloadfile = value
        elif op == "-m":
            mode = value
        elif op == "-h":
            usage()
            sys.exit()


def usage():
    print("usage:\n\
            -m <down/up> -- upload test or download test\n\
            -s <serial>  -- (/dev/ttyUSB0) uart port\n\
            -u <url>     -- server url\n\
            -f <file>    -- download file path\n\
            -a <apn>     -- (CMNET) maybe CMNET, UNINET ...\n")

if __name__ == "__main__":
    parseParam(sys.argv[1:])
    if mode == 'up':
        ftpprepare()
        uploadtest(uploadsize)
    elif mode == 'down':
        ftpprepare()
        downloadtest(downloadfile)
    else:
        usage()


