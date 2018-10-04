import unittest
import time
from common.atc import Attest

class Test_ECHO(unittest.TestCase):
      def setUp(self):
        print("测试开始")
        self.attester = Attest()

      def test_ECHO1(self):
            cmd = "AT+ECHO=0"
            self.attester.executeCmd(cmd)
            time.sleep(1)

            cmd = "AT+ECHO=?"
            expctedRes = ["+ok"]
            reallyRes=self.attester.executeCmd(cmd)
            print("执行命令：",cmd)
            print("真实响应：", reallyRes)
            print("期望响应：",expctedRes)
            self.assertEqual(reallyRes, expctedRes)

      def test_ECHO2(self):
            cmd = "AT+ECHO=0"
            expctedRes = ["+ok"]
            reallyRes=self.attester.executeCmd(cmd)
            print("执行命令：",cmd)
            print("真实响应：", reallyRes)
            print("期望响应：",expctedRes)
            self.assertEqual(reallyRes, expctedRes)

      def test_ECHO3(self):
            cmd = "AT+ECHO=1"
            self.attester.executeCmd(cmd)
            time.sleep(1)

            cmd = "AT+ECHO=1"
            expctedRes = ["AT+ECHO=1","+ok"]
            reallyRes = self.attester.executeCmd(cmd)
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
