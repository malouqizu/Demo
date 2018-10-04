#encoding:utf-8
import sys

def getAllContentFromTxt(path):
    allContent = ""
    f = open(path, "r")
    for line in f.readlines():
        allContent+=line
    f.close()
    return allContent

def getKeyAndValue(strSrc):
    strSrc = str(strSrc)
    strSrc = strSrc.replace("}","")
    strSrc = strSrc.replace("{", "")
    strSrc = strSrc.replace("]", "")
    strSrc = strSrc.replace("[", "")

    lstId=[]
    lstData=[]
    lstSplitWithComma = strSrc.split(",")
    for element in lstSplitWithComma:
        if"Id" in element:
            ele= element.split(":")
            lstId.append(ele[1])
        if "Data" in element:
            ele = element.split(":")
            lstData.append(ele[1])
    Data = ""
    Id = ""
    for d in lstData:
        Data= Data+d+"::"
    #print "\r\n"
    for i in lstId:
        Id= Id+i+"::"
    return Data.replace("\"",""), Id.replace("\"","")


if __name__=="__main__":

    if len(sys.argv)<2:
        print "Too few Argument";
        exit(-1);
    sys.stdout = open("./res.txt", "w")
    allContent = getAllContentFromTxt(sys.argv[1])
    Data,Id = getKeyAndValue(allContent)
    print Data
    print "\r\n"
    print Id


