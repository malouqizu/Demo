#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import random
import threading
from comm.atc import atLogger, atChat, atConfig, relayCtrl

class OFOTest(unittest.TestCase):
    """ Power on/off, sleep/awake test case """
    name = 'Test for OFO project'

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()
        relayCtrl.close_channel()

    def check_status(self):
        check_timeout = 10.0
        for n in range(20):
            if atChat.send_ok('AT', check_timeout):
                return True
        atLogger.case_log('There may be something wrong with chip!')
        return False

    def power_on_off(self):
        test_timeout = 30.0

        relayCtrl.close_channel()
        atChat.reopen()
        time.sleep(1.0)
        relayCtrl.open_channel()
        if not atChat.wait('+CREG: 1', 30.0):
            return False
        if not atChat.send_ok('ATE0', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CPIN?', test_timeout) or \
                not atChat.has('+CPIN:READY'):
            return False
        time.sleep(1)
        if not atChat.send('AT+CGREG?', test_timeout) or \
                not atChat.get_line_starts('+CGREG:'):
            return False
        time.sleep(1)
        if not atChat.send('AT+CSQ', test_timeout) or \
                not atChat.get_line_starts('+CSQ:'):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CIMI', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CGSN', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send('AT+CCED=0,1', test_timeout) or \
                not atChat.get_line_starts('+CCED:'):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CGMM', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CGMR', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send_ok('ATV1', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send('AT+CGREG?', test_timeout) or \
                not atChat.get_line_starts('+CGREG:'):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CGACT=0,1', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send('AT+CGACT?', test_timeout) or \
                not atChat.contain(',0'):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CGDCONT=1,"IP","CMNET"', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CGACT=1,1', test_timeout):
            return False
        time.sleep(1)
        if not atChat.send('AT+CGPADDR=1', test_timeout) or \
                not atChat.contain('.'):
            return False
        time.sleep(1)
        if not atChat.send('AT+CSQ', test_timeout) or \
                not atChat.get_line_starts('+CSQ:'):
            return False
        time.sleep(1)
        if not atChat.send('AT+CCED=0,1', test_timeout) or \
                not atChat.get_line_starts('+CCED:'):
            return False
        time.sleep(1)
        if not atChat.send('AT+CIPSTART="TCP","47.93.154.72",38483', test_timeout) \
                or not atChat.has('CONNECT OK'):
            return False
        time.sleep(1)
        if not atChat.send('AT+CIPSEND', test_timeout):
            atChat.send_ok('AT+CIPCLOSE', test_timeout)
            return False
        time.sleep(1)
        send_data = 'A0 00 00 01 00 30 46 30 17 01 12 34 57 FF 00 3F 01 01 00 01 00 30 46 30 17 01 12 34 57 FF 00 00 58 68 46 AC 10 32 64 82 01 01 00 00 0E 14 12 34 FF 00 00 00 00 00 00 00 00 00 00 58 68 46 AC 58 68 46 AC 02 00 00 00 00 00 00 00 00 00 00 00 40'
        if not atChat.send_ok(send_data+chr(26), test_timeout):
            atChat.send_ok('AT+CIPCLOSE', test_timeout)
            return False
        time.sleep(1)
        if not atChat.send_ok('AT+CIPCLOSE', test_timeout) or \
                not atChat.send_ok('AT+CIPSHUT', test_timeout):
            return False
        return True


    def sleep_awake(self):
        test_timeout = 30.0

        relayCtrl.close_channel()
        time.sleep(1.0)
        relayCtrl.open_channel()
        if not atChat.send_ok('AT+CSCLK=1', test_timeout):
            atLogger.case_log('Send sleep command failed!')
            time.sleep(1)
            relayCtrl.close_channel()
            return False
        atLogger.case_log('Sleeping...')
        sleeptime = random.randint(600, 1800)
        time.sleep(sleeptime)
        relayCtrl.close_channel()
        atLogger.case_log('Awake!')
        if not atChat.send_ok('AT+CIPSTART="TCP","47.93.154.72",38483', test_timeout) \
                or not atChat.has('CONNECT OK'):
            return False
        time.sleep(1.0)
        if not atChat.send('AT+CIPSEND', test_timeout):
            atChat.send('AT+CIPCLOSE', test_timeout)
            return False
        time.sleep(1.0)
        send_data = 'A0 00 00 01 00 30 46 30 17 01 12 34 57 FF 00 3F 01 01 00 01 00 30 46 30 17 01 12 34 57 FF 00 00 58 68 46 AC 10 32 64 82 01 01 00 00 0E 14 12 34 FF 00 00 00 00 00 00 00 00 00 00 58 68 46 AC 58 68 46 AC 02 00 00 00 00 00 00 00 00 00 00 00 40'
        if not atChat.send_ok(send_data+chr(26), test_timeout):
            atChat.send('AT+CIPCLOSE', test_timeout)
            return False
        time.sleep(1.0)
        if not atChat.send_ok('AT+CIPCLOSE', test_timeout) or \
                not atChat.send_ok('AT+CIPSHUT', test_timeout):
            return False
        return True


    def test_poweronoff(self):
        pass_cnt = 0
        testround = 10000
        for i in range(testround):
            atLogger.case_log('------------Test Round: %s ----------' % str(i+1))
            if not self.power_on_off():
                if not self.check_status():
                    break
                continue
            pass_cnt += 1
            atLogger.case_log('--Total test round: %s' % str(i+1))
            atLogger.case_log('--Success count: %s' % str(pass_cnt))
            atLogger.case_log('--Fail count: %s' % str(i+1-pass_cnt))
        atLogger.case_log('========================================')
        atLogger.case_log('--Total test round: %s' % str(i+1))
        atLogger.case_log('--Success count: %s' % str(pass_cnt))
        atLogger.case_log('--Fail count: %s' % str(i+1-pass_cnt))
        atLogger.case_log('--FPY: %s' % (str(pass_cnt / testround * 100) + '%'))
        self.assertTrue(pass_cnt == testround)

    
    def test_sleep_awake(self):
        pass_cnt = 0
        testround = 100
        test_timeout = 30.0
        self.assertTrue(atChat.send_ok('AT+CGATT=1', test_timeout))
        self.assertTrue(atChat.send_ok('AT+CGDCONT=1,"IP","CMNET"' , test_timeout))
        self.assertTrue(atChat.send_ok('AT+CGACT=1', test_timeout))
        for i in range(testround):                      
            atLogger.case_log('------------Test Round: %s ----------' % str(i+1))
            if not self.sleep_awake():
                if not self.check_status():
                    break
                continue
            pass_cnt += 1
            atLogger.case_log('--Total test round: %s' % str(i+1))
            atLogger.case_log('--Success count: %s' % str(pass_cnt))
            atLogger.case_log('--Fail count: %s' % str(i+1-pass_cnt))
        atLogger.case_log('========================================')
        atLogger.case_log('--Total test round: %s' % str(i+1))
        atLogger.case_log('--Success count: %s' % str(pass_cnt))
        atLogger.case_log('--Fail count: %s' % str(i+1-pass_cnt))
        atLogger.case_log('--FPY: %s' % (str(pass_cnt / testround * 100) + '%'))
        self.assertTrue(pass_cnt == testround)
