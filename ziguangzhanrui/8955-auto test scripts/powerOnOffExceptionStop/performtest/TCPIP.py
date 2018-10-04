import unittest
from powerOnOffExceptionStop.comm.atc import atLogger, atChat, relayCtrl
import time


class Tcpip(unittest.TestCase):
    """test case"""
    name = "Connect and disconnect TCP"

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_tcpconnect(self):
        connectavgtime = 0
        connectmaxtime = 0
        connectmintime = 1000
        connectsumtime = 0
        connectsuccesscnt = 0
        testround = 100
        self.assertTrue(atChat.send('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGDCONT=1,"IP","cmnet"', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGACT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            starttime = time.time()
            atChat.send('AT+CIPSTART="TCP","123.57.221.42",6805', 40.0)
            endtime = time.time()
            if atChat.has('CONNECT OK'):
                connectsuccesscnt += 1
                connectsumtime += (endtime - starttime)
                connectavgtime = connectsumtime / connectsuccesscnt
                if (endtime - starttime) > connectmaxtime:
                    connectmaxtime = endtime - starttime
                if (endtime - starttime) < connectmintime:
                    connectmintime = endtime - starttime
                atLogger.case_log('Time cost of connect TCP: %ss' % str(endtime - starttime))
                self.assertTrue(atChat.send('AT+CIPCLOSE', 40.0))
                self.assertTrue(atChat.has('OK'))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('TCP connect success count: %s' % str(connectsuccesscnt))
        atLogger.case_log('TCP connect FPY: %s' % (str(connectsuccesscnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of connect TCP is: %ss' % str(connectavgtime))
        atLogger.case_log('Max time cost of connect TCP is: %ss' % str(connectmaxtime))
        atLogger.case_log('Min time cost of connect TCP is: %ss' % str(connectmintime))
        self.assertTrue(connectsuccesscnt == testround)

    def test_tcpsidconnect(self):
        disconnectavgtime = 0
        disconnectmaxtime = 0
        disconnectmintime = 1000
        disconnectsumtime = 0
        disconnectsuccesscnt = 0
        testround = 100
        self.assertTrue(atChat.send('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGDCONT=1,"IP","cmnet"', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGACT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.case_log('Test Round: %s --------' % str(i + 1))
            if not atChat.send('AT+CIPSTART="TCP","123.57.221.42",6805', 40.0):
                continue
            if not atChat.has('CONNECT OK'):
                continue
            starttime = time.time()
            atChat.send('AT+CIPCLOSE', 40.0)
            endtime = time.time()
            if atChat.has('OK'):
                disconnectsuccesscnt += 1
                disconnectsumtime += (endtime - starttime)
                disconnectavgtime = disconnectsumtime / disconnectsuccesscnt
                if (endtime - starttime) > disconnectmaxtime:
                    disconnectmaxtime = endtime - starttime
                if (endtime - starttime) < disconnectmintime:
                    disconnectmintime = endtime - starttime
                atLogger.case_log('Time cost of disconnect TCP: %ss' % str(endtime - starttime))
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('TCP disconnect success count: %s' % str(disconnectsuccesscnt))
        atLogger.case_log('TCP disconnect FPY: %s' % (str(disconnectsuccesscnt / testround * 100) + '%'))
        atLogger.case_log('Average time cost of disconnect TCP is: %ss' % str(disconnectavgtime))
        atLogger.case_log('Max time cost of disconnect TCP is: %ss' % str(disconnectmaxtime))
        atLogger.case_log('Min time cost of disconnect TCP is: %ss' % str(disconnectmintime))
        self.assertTrue(disconnectsuccesscnt == testround)