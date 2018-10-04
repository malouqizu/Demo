import unittest
from comm.atlogger import atLogger
from comm.atchat import atChat
import time

class Test_S0_01(unittest.TestCase):
    name = "S0_01"

    @classmethod
    def setUpClass(cls):
        atLogger.case_start(cls.name)
        print("S0_01")
        time.sleep(10)
        atChat.com_open()

    def test_s0_01(self):
        self.result = False
        expected=["0-255","ok"]
        cmd="ats0=?"
        atChat.send_command(cmd)
        self.result=atChat.has_in_order(expected)
        self.assertTrue(self.result)

    @classmethod
    def tearDownClass(cls):
        atChat.com_close()
        atLogger.case_end(cls.name)

case_s0_01=Test_S0_01("test_s0_01")

if __name__=="__main__":
    case_s0_01=Test_S0_01("test_s0_01")

    suite=unittest.TestSuite()
    suite.addTest(case_s0_01)

    runner=unittest.TextTestRunner()
    runner.run(suite)

