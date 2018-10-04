#!/usr/bin/env python
# -*- coding: utf-8 -*-
from optparse import OptionParser
import time
import os
from urllib.parse import urlparse

print(os.environ.get('BUILD_NUMBER'))
print(os.environ.get('BUILD_ID'))

def traverDir(dirname,sourceStr,destStr):
    print(os.listdir(dirname))
    for i in os.listdir(dirname):
        print(i)
        pat = os.path.join(dirname, i)
        if os.path.isfile(pat):
            s='sed -i \"s/'+sourceStr+'/'+destStr+'/g\" ' + pat
            print(s)
            os.popen(s)
        else:
            traverDir(pat,sourceStr,destStr)

    return '文件内容替换完毕。'

traverDir('/home/limengmeng/test/','h','s')









