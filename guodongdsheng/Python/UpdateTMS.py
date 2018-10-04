#coding=utf-8

import os
import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print "请填写版本号"
        exit(-1)
    if os.system("cp -r /media/mat/DISK/TMS* ~/TMS_"+sys.argv[1]) is not 0:
        print "从优盘拷贝文件失败"
        exit(-1)
    if os.system("tasstop.sh"):
        print "停止TMS失败"
        exit(-1)
    if os.system("cp ~/TMS/TMS_"+sys.argv[1]+"/mat*.ear /______") is not 0:
        print "拷贝ear文件失败"
        exit(-1)

    os.system("cddum | ls")

    if os.system("tasstart.sh"):
        print "开启TMS失败"
        exit(-1)
    print "更新TMS成功"
