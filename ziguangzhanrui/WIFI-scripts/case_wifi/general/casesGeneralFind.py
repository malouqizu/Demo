import unittest
from case_wifi.general.case_AT import Test_AT
from case_wifi.general.case_ECHO import Test_ECHO
from case_wifi.general.case_H import Test_H
from case_wifi.general.case_RST import Test_RST
from case_wifi.general.case_SLEEP import Test_SLEEP
from case_wifi.general.case_UART import Test_UART
from case_wifi.general.case_VER import Test_VER

Test_AT_cases=unittest.TestLoader().loadTestsFromTestCase(Test_AT)
Test_ECHO_cases=unittest.TestLoader().loadTestsFromTestCase(Test_ECHO)
Test_H_cases=unittest.TestLoader().loadTestsFromTestCase(Test_H)
Test_RST_cases=unittest.TestLoader().loadTestsFromTestCase(Test_RST)
Test_SLEEP_cases=unittest.TestLoader().loadTestsFromTestCase(Test_SLEEP)
Test_UART_cases=unittest.TestLoader().loadTestsFromTestCase(Test_UART)
Test_VER_cases=unittest.TestLoader().loadTestsFromTestCase(Test_VER)

WifiCasesSuite=[Test_AT_cases,Test_ECHO_cases,Test_H_cases,Test_RST_cases,Test_SLEEP_cases,Test_VER_cases]

if __name__=="__main__":
    print(Test_AT_cases)
    print(Test_ECHO_cases)
    print(Test_H_cases)
    print(Test_RST_cases)
    print(Test_SLEEP_cases)
    print(Test_VER_cases)

    '''
    suite=unittest.TestSuite()
    suite.addTests(WifiCasesSuite)

    runner=unittest.TextTestRunner()
    runner.run(suite)
    '''


