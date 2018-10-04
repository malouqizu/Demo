#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from powerOnOffExceptionStop.comm.atc import atLogger, atChat, relayCtrl
import time

class PowerOnTime(unittest.TestCase):
    """test case"""
    name = 'Power On Time'

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        relayCtrl.close_channel()
        atChat.close()

    def test_01(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        failcnt = 0
        timeout = 30.0
        for i in range(100):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            relayCtrl.open_channel()
            starttime = time.time()
            while True:
                if time.time() > (starttime + timeout):
                    failcnt += 1
                    break
                if atChat.send('AT', 0.3):
                    endtime = time.time()
                    successcnt += 1
                    sumtime += (endtime - starttime)
                    avgtime = sumtime / successcnt
                    if (endtime - starttime) > maxtime:
                        maxtime = endtime - starttime
                    if (endtime - starttime) < mintime:
                        mintime = endtime - starttime
                    atLogger.case_log('Time cost: %ss' % str(endtime - starttime))
                    break
            relayCtrl.close_channel()
            time.sleep(2)
        atLogger.case_log('Total test round: %s' % str(successcnt + failcnt))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / (successcnt + failcnt) * 100) + '%'))
        atLogger.case_log('Average time cost of power on is: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of power on is: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of power on is: %ss' % str(mintime))
        self.assertTrue(failcnt == 0)