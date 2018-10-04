#coding: utf-8
import xml.dom.minidom
log = open("res.txt","a")
dom = xml.dom.minidom.parse("test_result.xml")
root = dom.documentElement
testCaseList = root.getElementsByTagName('TestCase')
for testCase in testCaseList:
    log.write("***********************************************************************\n")
    log.write(testCase.getAttribute("name")+"\n")
    testList = testCase.getElementsByTagName('Test')
    for test in testList:
        log.write(test.getAttribute("name")+"---"+test.getAttribute("result")+"\n")
