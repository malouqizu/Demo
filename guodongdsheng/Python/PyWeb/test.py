import xml.etree.cElementTree as ET
import sys

def open_xml(path):
    try:
        return ET.parse(path)
    except Exception as e:
        print(path,":", e)

def getInfoFromXML(path):
    tree = open_xml(path)
    for element in tree.iter():
        if element.tag == "TestCase":
            #print ("***********************************************************************")
            #print (element.attrib['name']+"\r\n")
            log.write("***********************************************************************\n")
            log.write(element.attrib['name']+"\r\n")
            for e in element.iter():
                if e.tag=="Test":
                    #print (e.attrib['name']+"----"+e.attrib['result']+"\r\n")
                    log.write(e.attrib['name']+"----"+e.attrib['result']+"\r\n")

if __name__=="__main__":
    log = open("res.txt","a")
    sys.stdout = log
    getInfoFromXML("./test_result.xml")
    #print ("sb DaJieZi good luck")