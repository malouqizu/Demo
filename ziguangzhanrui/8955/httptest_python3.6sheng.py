#!/usr/bin/env python
import time
import sys
import random
import serial
import getopt
import os

apn = 'CMNET'
mode = ''
port = 'COM42'

putfile = 'D:/file.3g2'

url = "http://123.57.221.42/"
urlWebdav = "http://123.57.221.42/webdav/"
httpsurl = "https://123.57.221.42/h263_amr_12.8k_9.87f_qcif.3g2"
httpurl = "http://123.57.221.42/h263_amr_12.8k_9.87f_qcif.3g2"
httpsprdurl="http://116.228.149.59/WAP/Download/Video/3gpp_video/h263_amr_12.8k_9.87f_qcif.3g2"
upuser = 'crethdom'
passwd = '123456'
contentype = 'text/plain'
contentname = 'put.txt'
bodycontent = 'helloworld'


downloadfile = os.path.basename(httpsurl)

write_once = 1440
read_once = 1024

def httpcmd(cmd):
    global ser
    ser.write(cmd.encode())
    #print(cmd)

def waitrsp(rsp):
    while(True):
        line = ser.readline()
        if (rsp.encode() in line):
            print('%s' % line.decode())
            break
        #else:
            #print('%s' % line.decode())
    return line
    
def httpprepare():
    global ser
    global port

    showconfig()
    ser=serial.Serial(port, 115200, rtscts=False, timeout=60)
    httpcmd("AT\r\n")
    waitrsp('OK')
    cmd = 'AT+CGDCONT=1,"IP","' + apn + '",\r\n'
    httpcmd(cmd)
    waitrsp('OK')
    httpcmd('AT+CGATT=1\r\n')
    waitrsp('OK')
    httpcmd('AT+CGACT=1,1\r\n')
    waitrsp('OK')

def downloadtest(file):
    cmd = 'AT+HTTPDOWNLOAD='+ httpsprdurl + '\r\n'
    httpcmd(cmd)
    waitrsp('contentLength')
    filesize = int(ser.readline())
    print('filesize:%d' % filesize)
    waitrsp('ready')

    dw_f = open(file, "wb+")
    left = filesize
    
    time_start = time.time()
    while left > 0:
        if left > read_once:
            readsize = read_once
        else:
            readsize = left

        line = ser.read(readsize)
        dw_f.write(line)
        rlen = len(line)
        left -= rlen
        print('readed:%d, left=%d' % (rlen, left))

    waitrsp('OK')
    
    time_end = time.time()
    
    dw_f.close()

def showconfig():
    print('url:' + url)
    print('mode:' + mode)
    print('serial:' + port)
    print('downloadfile:' + downloadfile)

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
            -m <down/author/get/post/put/head/options/trace/delete/> -- upload test or download test\n\
            -s <serial>  -- (/dev/ttyUSB0) uart port\n\
            -u <url>     -- server url\n\
            -f <file>    -- download file path\n\
            -h <help>    -- usage\n\
            -a <apn>     -- (CMNET) maybe CMNET, UNINET ...\n")

if __name__ == "__main__":
    parseParam(sys.argv[1:])
    httpprepare()
	
    if mode == "author":
        cmd = 'AT+HTTPAUTHOR='+ url + ',' + upuser + ',' + passwd + '\r\n'
    elif mode == "get":
        cmd = 'AT+HTTPGET='+ url + '\r\n'
    elif mode == "post":
        cmd = 'AT+HTTPPOST='+ url + ',' + contentype + ',' +bodycontent +'\r\n'
    elif mode == "put":
        cmd = 'AT+HTTPPUT='+ urlWebdav + ',' + contentype + ',' + contentname +',' +bodycontent +'\r\n'
    elif mode == "head":
        cmd = 'AT+HTTPHEAD='+ url + '\r\n'
    elif mode == "options":
        cmd = 'AT+HTTPOPTIONS='+ url + '\r\n'
    elif mode == "trace":
        cmd = 'AT+HTTPTRACE='+ url + '\r\n'
    elif mode == "delete":
	    cmd = 'AT+HTTPDELETE='+ urlWebdav + ',' + contentname +'\r\n'
    elif mode == "down":
        downloadtest(downloadfile)
        sys.exit()
    else:
        print('Do not support this method.')
        sys.exit()
	
	
    if cmd.strip:
        httpcmd(cmd)
        waitrsp('OK')
    else:
	    print("Cmd is null")
    


