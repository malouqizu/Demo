import unittest
from comm.atlogger import atLogger
from comm.atchat import atChat
import time

class Test_S0_02(unittest.TestCase):
    name = "S0_02"

    @classmethod
    def setUpClass(cls):
        atLogger.case_start(cls.name)
        print("S0_02")
        time.sleep(10)
        atChat.com_open()

    def test_s0_02(self):
        self.result = False
        expected=["0","ok"]
        atChat.send_command("ats0=0")
        if atChat.has("ok"):
            atChat.send_command("ats0?")
            self.result = atChat.has_in_order(expected)
        else:
            self.result=False

        self.assertTrue(self.result)

    @classmethod
    def tearDownClass(cls):
        atChat.com_close()
        atLogger.case_end(cls.name)

case_s0_02=Test_S0_02("test_s0_02")

if __name__=="__main__":
    case_s0_02=Test_S0_02("test_s0_02")

    suite=unittest.TestSuite()
    suite.addTest(case_s0_02)

    runner=unittest.TextTestRunner()
    runner.run(suite)

