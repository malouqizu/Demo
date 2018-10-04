#encoding:utf-8
import sys
import os
from xml.etree import ElementTree as ET

def changeRootAttribAndSave(casePath):
    xmldoc = ET.parse(casePath)
    root = xmldoc.getroot()
    # attNames = root.attrib.keys()
    # for i in attNames:
        # del root.attrib[i]
    root.attrib.clear()
    root.attrib["logicName"] = ""
    root.attrib["description"] = ""
    root.attrib["logcatEnabled"] = "true"
    root.attrib["memoryEnabled"] = "false"
    root.attrib["memTime"] = "0"
    root.attrib["memTestPackage"] = ""
    root.attrib["cpuTime"] = ""
    root.attrib["eventsEnabled"] = "false"
    root.attrib["radioEnabled"] = "false"
    root.attrib["kernelEnabled"] = "false"
    root.attrib["monkeyEnabled"] = "false"
    xmldoc.write("./new/"+casePath, "utf-8")

if __name__=="__main__":
    caseList = os.listdir(".")
    for case in caseList:
        print case


