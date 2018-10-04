import time
import unittest
from common.atc import Attest

class Test_AT(unittest.TestCase):
      def setUp(self):
        print("测试开始")
        self.attester = Attest()

      def test_AT(self):
            cmd = "AT+ECHO=0"
            self.attester.executeCmd(cmd)
            time.sleep(1)

            cmd = "AT"
            expctedRes = ["+ok"]
            reallyRes=self.attester.executeCmd(cmd)
            print("执行命令：",cmd)
            print("真实响应：", reallyRes)
            print("期望响应：",expctedRes)
            self.assertEqual(reallyRes, expctedRes)

      def tearDown(self):
          self.attester.attest_close()
          print("测试结束\n")

if __name__=="__main__":
      #此语句可以执行所有测试用例
      unittest.main()
