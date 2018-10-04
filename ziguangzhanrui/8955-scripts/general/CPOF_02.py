import unittest
from comm.atlogger import atLogger
from comm.atchat import atChat
import time

class Test_CPOF_02(unittest.TestCase):
    name = "CPOF_02"

    @classmethod
    def setUpClass(cls):
        atLogger.case_start(cls.name)
        print("CPOF_02")
        time.sleep(10)
        atChat.com_open()

    def test_cpof_02(self):
        self.result = False
        cmd="at+cpof"
        atChat.send_command(cmd)
        if atChat.has("OK"):
            time.sleep(30)
            atChat.send_command("at")
            if atChat.has("OK"):
                self.result=True
            else:
                self.result=False
        else:
            self.result=False

        self.assertTrue(self.result)

    @classmethod
    def tearDownClass(cls):
        atChat.com_close()
        atLogger.case_end(cls.name)

case_cpof_02=Test_CPOF_02("test_cpof_02")

if __name__=="__main__":
    case_cpof_02=Test_CPOF_02("test_cpof_02")

    suite=unittest.TestSuite()
    suite.addTest(case_cpof_02)

    runner=unittest.TextTestRunner()
    runner.run(suite)


