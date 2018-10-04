#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from powerOnOffExceptionStop.comm.atc import atLogger, atChat, atConfig
import time
import random


def random_str(randomlength):
     str = ''
     chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
     length = len(chars) - 1
     for i in range(randomlength):
         str += chars[random.randint(0, length)]
     return str


class BuildInConnect(unittest.TestCase):
    """test case"""
    name = "Build In Connect"
    timeout_cmd = 1.0
    timeout_cgatt = 30.0
    timeout_cgact = 30.0
    timeout_ip = 100.0

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_shortshort(self):
        successcnt = 0
        tcpfailcnt = 0
        testround = 100
        self.assertTrue(atChat.send_ok('AT+CGATT=1', self.timeout_cgatt))
        self.assertTrue(atChat.send_ok('AT+COPS?', self.timeout_cmd))
        if atChat.contain('46001') or atChat.contain('46009'):
            apn = '3gnet'
        elif atChat.contain('46000') or atChat.contain('46002') or \
                atChat.contain('46007') or atChat.contain('46008'):
            apn = 'cmnet'
        else:
            return
        self.assertTrue(atChat.send_ok('AT+CGDCONT=1,"IP","%s"' % (apn), self.timeout_cmd))
        for i in range(testround):
            self.assertTrue(tcpfailcnt < 3)
            atLogger.case_log('------------Test Round: %s ----------' % str(i+1))
            if not atChat.send_ok('AT+CGACT=1', self.timeout_cgact):
                continue
            if not atChat.send_ok('AT+CIPSTART="TCP","%s",%d' %
                                  (atConfig.echo_server, atConfig.echo_port), self.timeout_ip):
                tcpfailcnt += 1
                continue
            tcpfailcnt = 0
            strlen = random.randint(1, 2048)
            randstr = random_str(strlen)
            if not atChat.send('AT+CIPSEND', self.timeout_ip) or \
                    not atChat.send(randstr+chr(26), self.timeout_ip) or \
                    not atChat.wait(randstr, self.timeout_ip):
                atChat.send('AT+CIPCLOSE', self.timeout_ip)
                continue
            if not atChat.send_ok('AT+CIPCLOSE', self.timeout_ip) or \
                    not atChat.send_ok('AT+CGACT=0', self.timeout_cgact):
                continue
            successcnt += 1
            atLogger.case_log('--Total test round: %s' % str(i+1))
            atLogger.case_log('--Success count: %s' % str(successcnt))
        atLogger.case_log('========================================')
        atLogger.case_log('--Total test round: %s' % str(testround))
        atLogger.case_log('--Success count: %s' % str(successcnt))
        atLogger.case_log('--FPY: %s' % (str(successcnt / testround * 100) + '%'))
        self.assertTrue(successcnt == testround)

    @unittest.skip('')
    def test_longshort(self):
        successcnt = 0
        tcpfailcnt = 0
        testround = 100
        self.assertTrue(atChat.send_ok('AT+CGATT=1', self.timeout_cgatt))
        self.assertTrue(atChat.send_ok('AT+COPS?', self.timeout_cmd))
        if atChat.contain('46001') or atChat.contain('46009'):
            apn = '3gnet'
        elif atChat.contain('46000') or atChat.contain('46002') or \
                atChat.contain('46007') or atChat.contain('46008'):
            apn = 'cmnet'
        else:
            return
        self.assertTrue(atChat.send_ok('AT+CGDCONT=1,"IP","%s"' % (apn), self.timeout_cmd))
        self.assertTrue(atChat.send_ok('AT+CGACT=1', self.timeout_cgact))
        for i in range(testround):
            self.assertTrue(tcpfailcnt < 3)
            atLogger.case_log('-------------Test Round: %s -----------' % str(i + 1))
            if not atChat.send_ok('AT+CIPSTART="TCP","%s",%d' %
                                  (atConfig.echo_server, atConfig.echo_port), self.timeout_ip):
                tcpfailcnt += 1
                continue
            tcpfailcnt = 0
            strlen = random.randint(1, 2048)
            randstr = random_str(strlen)
            if not atChat.send('AT+CIPSEND', self.timeout_ip) or\
                    not atChat.send(randstr + chr(26), self.timeout_ip) or \
                    not atChat.wait(randstr, self.timeout_ip):
                atChat.send('AT+CIPCLOSE', self.timeout_ip)
                continue
            if not atChat.send_ok('AT+CIPCLOSE', self.timeout_ip):
                continue
            successcnt += 1
            atLogger.case_log('--Total test round: %s' % str(testround))
            atLogger.case_log('--Success count: %s' % str(successcnt))
        self.assertTrue(atChat.send_ok('AT+CGACT=0', self.timeout_cgact))
        atLogger.case_log('========================================')
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        self.assertTrue(successcnt == testround)

    @unittest.skip('')
    def test_longlong(self):
        successcnt = 0
        testround = 100
        self.assertTrue(atChat.send_ok('AT+CGATT=1', self.timeout_cgatt))
        self.assertTrue(atChat.send_ok('AT+COPS?', self.timeout_cmd))
        if atChat.contain('46001') or atChat.contain('46009'):
            apn = '3gnet'
        elif atChat.contain('46000') or atChat.contain('46002') or \
                atChat.contain('46007') or atChat.contain('46008'):
            apn = 'cmnet'
        else:
            return
        self.assertTrue(atChat.send_ok('AT+CGDCONT=1,"IP","%s"' % (apn), self.timeout_cmd))
        self.assertTrue(atChat.send_ok('AT+CGACT=1', self.timeout_cgact))
        self.assertTrue(atChat.send_ok('AT+CIPSTART="TCP","%s",%d' %
                                       (atConfig.echo_server, atConfig.echo_port), self.timeout_ip))
        for i in range(testround):
            atLogger.case_log('--------------Test Round: %s ------------' % str(i + 1))
            strlen = random.randint(1, 2048)
            randstr = random_str(strlen)
            if not atChat.send('AT+CIPSEND', self.timeout_ip) or\
                    not atChat.send(randstr + chr(26), self.timeout_ip) or\
                    not atChat.wait(randstr, self.timeout_ip):
                continue
            successcnt += 1
            atLogger.case_log('--Total test round: %s' % str(testround))
            atLogger.case_log('--Success count: %s' % str(successcnt))
        self.assertTrue(atChat.send_ok('AT+CIPCLOSE', self.timeout_ip))
        self.assertTrue(atChat.send_ok('AT+CGACT=0', self.timeout_cgact))
        atLogger.case_log('========================================')
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        self.assertTrue(successcnt == testround)

