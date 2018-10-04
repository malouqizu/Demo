# encoding: utf-8
import os
import sys
default_encoding = 'utf-8'

def rename():
    path="./"
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files);#原来的文件路径
        filename=os.path.splitext(files)[0];#文件名
        filetype=os.path.splitext(files)[1];#文件扩展名
        filename = filename.replace("传智播客","")
        Newdir=os.path.join(path,filename+filetype);#新的文件路径
        os.rename(Olddir,Newdir);#重命名

if __name__=="__main__":
    # reload(sys)
    # sys.setdefaultencoding(default_encoding)
    #rename();

    print "完颜兀术"
