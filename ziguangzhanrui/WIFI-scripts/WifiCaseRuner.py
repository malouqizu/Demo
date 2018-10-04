import time
import sys
import unittest
from HTML.HTMLTestRunner import HTMLTestRunner
from case_wifi.general.casesGeneralFind import WifiCasesSuite

if __name__=="__main__":
    #print(sys.path)
    curTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename="WIFIFunTestReport"+curTime+".html"
    fp=open('E:/demo/Python/project88/WifiHtmlReport/'+filename, 'wb')

    runner=HTMLTestRunner(
        stream=fp,
        title='My WIFI Function Unit Test Report',
        description='This demonstrates the report output by HTMLTestRunner.'
    )

    suite = unittest.TestSuite()
    suite.addTests(WifiCasesSuite)
    runner.run(suite)
    print(WifiCasesSuite)

