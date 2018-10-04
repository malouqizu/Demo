#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from powerOnOffExceptionStop.comm.atc import atLogger, atChat, relayCtrl
import time

class RegisterNet(unittest.TestCase):
    """ test case """
    name = "RegisterNet"

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
        testround = 100
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i+1))
            relayCtrl.open_channel()
            starttime = time.time()
            if atChat.wait('+CREG: 1', 30.0):
                endtime = time.time()
                secdcost = endtime - starttime
                successcnt += 1
                sumtime += secdcost
                avgtime = sumtime / successcnt
                if secdcost > maxtime:
                    maxtime = secdcost
                if secdcost < mintime:
                    mintime = secdcost
                atLogger.case_log('Time cost: %ss' % str(secdcost))
            relayCtrl.close_channel()
            time.sleep(1)
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of register net is: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of register net is: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of register net is: %ss' % str(mintime))
        self.assertTrue(successcnt == testround)
