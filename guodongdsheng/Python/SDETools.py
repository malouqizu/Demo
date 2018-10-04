#coding:utf-8
import os
import sys

def getContent(path):
    f = open(path, "r")
    lines = f.readlines()
    content = ""
    for line in lines:
        content += line.strip().replace("\r\n", "")
    return content

def getFileDict(path):
    d = dict()
    fileList = os.listdir(path)
    for item in fileList:
        if not item.endswith("xml"):
            fileList.remove(item)

    for item in fileList:
        fileContent = getContent(path + "/" +item)
        d[item] = fileContent

    return d




if __name__== "__main__":

    if len(sys.argv)<3:
        print "too few argument"
        exit(-1)
    templatesPath = sys.argv[1]
    sdePath = sys.argv[2]

    print templatesPath
    print sdePath

    f = open( "./res.log", "w")
    sys.stdout = f

    templatesDict =  getFileDict(templatesPath)
    sdeDict = getFileDict(sdePath)
    for k in templatesDict.keys():
        try:
            if templatesDict[k] == sdeDict[k]:
                #print k+"is OK"
                pass
            else:
                print "\n-----------------------------------"
                print k+"\n"
                print templatesDict[k]
                print sdeDict[k]
        except Exception as e:
                print str(e)+"no file"


