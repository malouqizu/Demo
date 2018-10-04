#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from powerOnOffExceptionStop.comm.atc import atLogger, atChat, relayCtrl, COMPORT
import time

class PowerOnTime(unittest.TestCase):
    """test case"""
    name = 'Power On'

    #所有测试用例共用此函数，就是说只执行一次此函数，可以节省时间
    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    # 所有测试用例共用此函数，就是说只执行一次此函数，可以节省时间
    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def check_status(self):
        check_timeout = 10.0
        for n in range(20):
            if atChat.send_ok('AT', check_timeout):
                return True
        atLogger.case_log('There may be something wrong with chip!')
        return False

    def test_01(self):
        successcnt = 0
        failcnt = 0
        timeout = 30.0
        testround = 1000
        for i in range(testround):
            atLogger.case_log('--------------Test Round: %s--------------' % (str(i + 1)))
            atLogger.case_log('--------------On: %s--------------' % COMPORT)
            relayCtrl.close_channel()
            time.sleep(1.0)
            relayCtrl.open_channel()
            time.sleep(timeout)
            if not self.check_status():
                failcnt += 1
                break
            successcnt += 1
        atLogger.case_log('Total test round: %s' % str(successcnt + failcnt))
        atLogger.case_log('Success count: %s' % str(successcnt))
        self.assertTrue(failcnt == 0)

if __name__ == '__main__':
    unittest.main()
