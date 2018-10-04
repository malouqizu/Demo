#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.atc import atLogger, atChat, relayCtrl
import time


class SleepAwakeTest(unittest.TestCase):
    """test case"""
    name = 'Sleep Awake Test'

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_01(self):
        successcnt = 0
        failcnt = 0
        timeout = 60.0
        i = 0
        while True:
            atLogger.case_log('------------Test Round: %s --------' % str(i + 1))
            relayCtrl.open_channel()
            atLogger.case_log('Sleeping...')
            time.sleep(10.0)
            relayCtrl.close_channel()
            starttime = time.time()
            while True:
                if time.time() > (starttime + timeout):
                    failcnt += 1
                    atLogger.case_log('Failed!!!')
                    break
                if atChat.send('AT', 0.5):
                    if atChat.has('OK'):
                        successcnt += 1
                        atLogger.case_log('Pass')
                        break
            if failcnt:
                break
            i += 1
        atLogger.case_log('====================================================')
        atLogger.case_log('Total test round: %s' % str(successcnt + failcnt))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('Fail count: %s' % str(failcnt))
        self.assertTrue(failcnt == 0)
