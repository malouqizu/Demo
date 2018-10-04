#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from powerOnOffExceptionStop.comm.atc import atLogger, atChat
import time


class AttachActive(unittest.TestCase):
    """ test case """
    name = "AttachActive"

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_attachactive(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            atChat.send('AT+CGATT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CGATT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            attachtime = endtime - starttime
            atChat.send('AT+CGACT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CGACT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            activetime = endtime - starttime
            successcnt += 1
            sumtime += (attachtime+activetime)
            avgtime = sumtime/successcnt
            if (activetime+attachtime) > maxtime:
                maxtime = (attachtime+activetime)
            if (activetime+attachtime) < mintime:
                mintime = (attachtime+activetime)
            atLogger.case_log('Time cost; %ss' % str(attachtime+activetime))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of attach and active: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of attach and active: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of attach and active: %ss' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_attach(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            atChat.send('AT+CGATT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CGATT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            attachtime = endtime - starttime
            successcnt += 1
            sumtime += attachtime
            avgtime = sumtime / successcnt
            if attachtime > maxtime:
                maxtime = attachtime
            if attachtime < mintime:
                mintime = attachtime
            atLogger.case_log('Time cost; %ss' % str(attachtime))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of attach: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of attach: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of attach: %ss' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_detach(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            atChat.send('AT+CGATT=1', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CGATT=0', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            detachtime = endtime - starttime
            successcnt += 1
            sumtime += detachtime
            avgtime = sumtime / successcnt
            if detachtime > maxtime:
                maxtime = detachtime
            if detachtime < mintime:
                mintime = detachtime
            atLogger.case_log('Time cost; %ss' % str(detachtime))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of detach: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of detach: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of detach: %ss' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_active(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        self.assertTrue(atChat.send('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            atChat.send('AT+CGACT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CGACT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            activetime = endtime - starttime
            successcnt += 1
            sumtime += activetime
            avgtime = sumtime / successcnt
            if activetime > maxtime:
                maxtime = activetime
            if activetime < mintime:
                mintime = activetime
            atLogger.case_log('Time cost; %ss' % str(activetime))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of active: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of active: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of active: %ss' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_deactivation(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        self.assertTrue(atChat.send('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            atChat.send('AT+CGACT=1', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CGACT=0', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            deactivationtime = endtime - starttime
            successcnt += 1
            sumtime += deactivationtime
            avgtime = sumtime / successcnt
            if deactivationtime > maxtime:
                maxtime = deactivationtime
            if deactivationtime < mintime:
                mintime = deactivationtime
            atLogger.case_log('Time cost; %ss' % str(deactivationtime))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of deactivation: %ss' % str(avgtime))
        atLogger.case_log('Max time cost of deactivation: %ss' % str(maxtime))
        atLogger.case_log('Min time cost of deactivation: %ss' % str(mintime))
        self.assertTrue(successcnt == testround)

 