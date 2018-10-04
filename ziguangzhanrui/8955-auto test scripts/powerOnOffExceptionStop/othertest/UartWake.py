#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from comm.atc import atLogger, atChat


class UartWakeTest(unittest.TestCase):
    """ Wakeup by UART_RXD GPIO """
    name = 'Uart Wake Test'
    timeout_cmd = 1.0

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_uart_wake(self):
        pass_cnt = 0
        fail_cnt = 0
        atChat.send("AT+CSCLK=2", self.timeout_cmd)
        for i in range(10):
            atLogger.case_timed_log('Test Round: %d' % (i + 1))

            # sleep to let module in
            time.sleep(5.0)

            # try several AT to wake up module, till OK is received
            for n in range(16):
                if atChat.send_ok("AT", 0.1):
                    break

            if not atChat.send_ok("AT+CSCLK=0", self.timeout_cmd) or \
                    not atChat.sleep(2.0) or \
                    not atChat.send_ok("AT+CSCLK=2", self.timeout_cmd):
                fail_cnt += 1
            else:
                pass_cnt += 1

            atLogger.case_log("Pass %d, fail %d" %(pass_cnt, fail_cnt))
        self.assertTrue(fail_cnt == 0)
