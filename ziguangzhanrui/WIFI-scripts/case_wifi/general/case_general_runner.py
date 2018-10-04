import unittest
from HTML.HTMLTestRunner import HTMLTestRunner
import time
from case_wifi.general.casesGeneralFind import WifiCasesSuite

if __name__=="__main__":
    curTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename="WIFIFunTestReport"+curTime+".html"
    fp=open('E:/demo/Python/project88/report/'+filename, 'wb')

    runner=HTMLTestRunner(
        stream=fp,
        title='My WIFI Function Unit Test Report',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    suite = unittest.TestSuite()
    suite.addTests(WifiCasesSuite)
    runner.run(suite)


