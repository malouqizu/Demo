import unittest
import time
from common.atc import Attest

class Test_H(unittest.TestCase):
      def setUp(self):
        print("测试开始")
        self.attester = Attest()

      def test_H(self):
          cmd = "AT+ECHO=0"
          self.attester.executeCmd(cmd)
          time.sleep(1)

          cmd = "AT+H"
          expctedRes = ["AT                 - AT mode",
                  "AT+H               - check AT help",
                  "AT+ECHO            - open/close uart echo",
                  "AT+RST             - Software Reset",
                  "AT+VER             - get version",
                  "AT+UART            - set/get serial baudrate",
                  "AT+WDBG            - adjust debug level",
                  "AT+USERDATA        - write/read user data",
                  "AT+SLEEP           - enable/disable sleep",
                  "AT+USERSLEEP       - set user sleep",
                  "AT+WAKESRC         - set wakeup source",
                  "AT+BOOTADDR        - set boot addr, HEX format",
                  "AT+RWFILE          - read/write FAT file",
                  "AT+RESTORE         - restore default config",
                  "AT+BOOTADDR        - do bootaddr",
                  "AT+WSMAC           - set/get mac address",
                  "AT+WSSCAN          - scan AP",
                  "AT+WSCONN          - start wifi connect",
                  "AT+WSDISCONN       - disconnect",
                  "AT+WSC             - start smart config",
                  "AT+WSFIXIP         - enable/disable DHCP",
                  "AT+WAP             - enable AP",
                  "AT+WAPSTOP         - stop AP",
                  "AT+WAMAC           - set/get softap mac address",
                  "AT+WSSAK           - start wechat airkiss",
                  "AT+WASTA           - get joined sta info",
                  "AT+WANET           - set/get AP net info",
                  "AT+NSTART          - start tcp/udp client",
                  "AT+NSTOP           - stop tcp/udp client",
                  "AT+NSEND           - send tcp/udp data",
                  "AT+NMODE           - start transparent transmission mode",
                  "AT+NLINK           - check tcp/udp client status",
                  "AT+NPING           - do ping",
                  "AT+NDNS            - do dns"]

          reallyRes = self.attester.executeCmd(cmd)
          print("执行命令：", cmd)
          print("真实响应：", reallyRes)
          print("期望响应：", expctedRes)
          self.assertEqual(reallyRes, expctedRes)

      def tearDown(self):
          self.attester.attest_close()
          print("测试结束\n")

if __name__=="__main__":
        #使用下面一系列语句实现执行本模块所有测试case，等价于unittest.main()语句
        suite=unittest.TestSuite()
        case_H=Test_H("test_ATH1")
        suite.addTest(case_H)
        runner=unittest.TextTestRunner
        runner.run(suite)


