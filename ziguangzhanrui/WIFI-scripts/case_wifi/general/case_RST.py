import unittest
import time
from common.atc import Attest

class Test_RST(unittest.TestCase):
      def setUp(self):
        print("测试开始")
        self.attester = Attest()

      def test_RST(self):
            cmd1 = "AT+RST"
            print("执行命令：", cmd1)
            self.attester.executeCmd(cmd1)
            time.sleep(10)

            cmd2="AT+ECHO=0"
            print("执行命令：", cmd2)
            self.attester.executeCmd(cmd2)
            time.sleep(3)

            cmd3="AT"
            print("执行命令：", cmd3)
            expctedRes = ["+ok"]
            reallyRes=self.attester.executeCmd(cmd3)
            print("真实响应：",reallyRes)
            print("期望响应：",expctedRes)
            self.assertEqual(reallyRes, expctedRes)

      def tearDown(self):
          self.attester.attest_close()
          print("测试结束\n")

if __name__=="__main__":
      #此语句可以执行所有测试用例
      unittest.main()