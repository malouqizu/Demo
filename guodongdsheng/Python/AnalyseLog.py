#encoding:"uft-8"
from __future__ import division
import os
import sys


countNotMatch = 0
countRecogniseMiss = 0
countRecogniseSuccess = 0

class LogInfo:
    def __init__(self):
        self.logAbsPath = ""
        self.beforeLine = ""
        self.currentLine = ""

    def getLineLastItemBySplit(self, mark, targetStr):
        tempList = targetStr.split(mark)
        tempLastItem = tempList[len(tempList) - 1]
        return tempLastItem

    def getFileName(self):
        if self.logAbsPath is "":
            print "ads path is null"
        else:
            lst = self.logAbsPath.split("/");
            countItem = len(lst);
            return lst[countItem - 2]


def analyLog(absPath):
    global countNotMatch
    global countRecogniseMiss
    global countRecogniseSuccess

    logNotMatch = 0
    logRecogniseMiss = 0
    logRecogniseSuccess = 0

    first = True
    logInfo = LogInfo()
    logInfo.logAbsPath = absPath
    lst = []
    expectedValue=""
    actualValue=""
    with open(absPath, "r") as f:
        for line in f.readlines():    
            line = line.strip()       
            if first is True:
                logInfo.beforeLine = line
                logInfo.currentLine = line
                first = False
            else:
                logInfo.beforeLine = logInfo.currentLine
                logInfo.currentLine = line

                if "expected" in logInfo.beforeLine:
                    expectedValue = logInfo.beforeLine[logInfo.beforeLine.rfind(":")+1:]
                    actualValue = logInfo.currentLine[logInfo.currentLine.rfind(":")+1:]

                if " No match found." in logInfo.beforeLine and " No match found." in logInfo.currentLine:
                    logNotMatch+=1
                    countNotMatch += 1

                elif "NOT match" in logInfo.beforeLine and "DejavuVR [failed]" in logInfo.currentLine:  
                    lst.append("expected:"+expectedValue)
                    lst.append("actualValue:"+actualValue)
                    logRecogniseMiss+=1
                    countRecogniseMiss += 1              
                    
                elif "Dejavu recongise match" in logInfo.beforeLine and "DejavuVR [finished]" in logInfo.currentLine:
                    logRecogniseSuccess+=1
                    countRecogniseSuccess += 1            
    
    print "\n",logInfo.getFileName()+":"
    print "not match found : ",logNotMatch
    print "miss : ",logRecogniseMiss
    if len(lst)>0:
        for item in lst:
            print item
    print "success : ",logRecogniseSuccess
    
            
def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file).replace("\\", "/"))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file).replace("\\", "/"))
            else:
                files_list.append(os.path.join(root, special_file).replace("\\", "/"))
    return files_list


if __name__ == "__main__":
    sys.argv[0] = "D:\\Untitled Folder\\VR\\811"
    list_logs = scan_files(sys.argv[0], None, "case-runner.log")

    f= open( sys.argv[0]+"/res.log","w")
    sys.stdout = f
    print "本次共统计了",len(list_logs),"个文件"
    for log in list_logs:
        analyLog(log)
    print "\n","countNotMatch:",countNotMatch
    print "countRecogniseMiss:",countRecogniseMiss
    print "countRecogniseSuccess:",countRecogniseSuccess

    count = countNotMatch+countRecogniseMiss+countRecogniseSuccess  
    print "Not match rate：","%.2f" % ((countNotMatch/count)*100),"%"
    print "Miss rate：", "%.2f" % ((countRecogniseMiss/count)*100),"%"
    print "Success rate：","%.2f" % ((countRecogniseSuccess/count)*100),"%"

    f.close()