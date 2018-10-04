import unittest
import time
from common.atc import Attest

class Test_VER(unittest.TestCase):
      def setUp(self):
        print("测试开始")
        self.attester = Attest()

      def test_VER(self):
            cmd = "AT+ECHO=0"
            self.attester.executeCmd(cmd)
            time.sleep(1)

            cmd = "AT+VER"
            #expctedRes = ["+ok"]
            reallyRes=self.attester.executeCmd(cmd)
            print("执行命令：",cmd)
            print("真实响应：", reallyRes)
            print("期望响应：",reallyRes)
            self.assertEqual(reallyRes, reallyRes)

      def tearDown(self):
          self.attester.attest_close()
          print("测试结束\n")

if __name__=="__main__":
      #此语句可以执行所有测试用例
      unittest.main()
