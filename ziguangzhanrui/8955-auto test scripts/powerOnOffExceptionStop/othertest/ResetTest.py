#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.atc import atLogger, atChat, relayCtrl
import time


class ResetTest(unittest.TestCase):
    """test case"""
    name = 'Reset Test'

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_vbat(self):
        successcnt = 0
        failcnt = 0
        timeout = 60.0
        i = 0
        while True:
            atLogger.case_log('------------Test Round: %s --------' % str(i + 1))
            relayCtrl.open_channel()
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
            relayCtrl.close_channel()
            i += 1
            time.sleep(2)
        atLogger.case_log('====================================================')
        atLogger.case_log('Total test round: %s' % str(successcnt + failcnt))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('Fail count: %s' % str(failcnt))
        self.assertTrue(failcnt == 0)

    def test_vrtc(self):
        successcnt = 0
        failcnt = 0
        timeout = 60.0
        i = 0
        while True:
            atLogger.case_log('------------Test Round: %s --------' % str(i + 1))
            relayCtrl.close_channel()
            time.sleep(5)
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
            relayCtrl.open_channel()
            i += 1
            time.sleep(2)
        atLogger.case_log('====================================================')
        atLogger.case_log('Total test round: %s' % str(successcnt + failcnt))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('Fail count: %s' % str(failcnt))
        self.assertTrue(failcnt == 0)