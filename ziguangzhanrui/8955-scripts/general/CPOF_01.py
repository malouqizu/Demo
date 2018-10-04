import unittest
from comm.atlogger import atLogger
from comm.atchat import atChat
import time

class Test_CPOF_01(unittest.TestCase):
    name = "CPOF_01"

    @classmethod
    def setUpClass(cls):
        atLogger.case_start(cls.name)
        print("CPOF_01")
        time.sleep(10)
        atChat.com_open()

    def test_cpof_01(self):
        self.result = False
        cmd="at+cpof=?"
        atChat.send_command(cmd)
        self.result=atChat.has("ok")

        self.assertTrue(self.result)

    @classmethod
    def tearDownClass(cls):
        atChat.com_close()
        atLogger.case_end(cls.name)

case_cpof_01=Test_CPOF_01("test_cpof_01")

if __name__=="__main__":
    case_cpof_01=Test_CPOF_01("test_cpof_01")

    suite=unittest.TestSuite()
    suite.addTest(case_cpof_01)

    runner=unittest.TextTestRunner()
    runner.run(suite)


