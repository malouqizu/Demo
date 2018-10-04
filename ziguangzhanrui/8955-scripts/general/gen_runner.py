import time
import unittest
from HTMLreport import HTMLTestRunner
from general.CPOF_01 import case_cpof_01
from general.CPOF_02 import case_cpof_02
from general.S0_01 import case_s0_01
from general.S0_02 import case_s0_02

general_cases=[case_cpof_01,case_cpof_02,case_s0_01,case_s0_02]
general_casesSuite=unittest.TestSuite()
general_casesSuite.addTests(general_cases)

curTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
filename="TestReport"+curTime+".html"
fp=open('E:/Python/demo/Auto-test-scripts/8955-scripts/report/'+filename, 'wb')

#runner=unittest.TextTestRunner()
htmlRunner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='My Calculator Function Unit Test Report',
        description='This demonstrates the report output by HTMLTestRunner.')

if __name__=="__main__":
   #runner.run(general_casesSuite)
   htmlRunner.run(general_casesSuite)

