import time
import unittest
from comm.atchat import atChat
from comm.atlogger import atLogger

class Tcpip(unittest.TestCase):
    """test case"""
    name = "Connect and disconnect TCP"

    @classmethod
    def setUpClass(cls):
        atLogger.case_start(cls.name)
        atChat.com_open()

    @classmethod
    def tearDownClass(cls):
        atChat.com_close()
        atLogger.case_end(cls.name)

    def test_tcpconnect(self):
        connectavgtime = 0
        connectmaxtime = 0
        connectmintime = 1000
        connectsumtime = 0
        connectsuccesscnt = 0
        testround = 100
        self.assertTrue(atChat.send_command('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send_command('AT+CGDCONT=1,"IP","cmnet"', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send_command('AT+CGACT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            starttime = time.time()
            atChat.send_command('AT+CIPSTART="TCP","123.57.221.42",6805', 40.0)
            endtime = time.time()
            if atChat.has('CONNECT OK'):
                connectsuccesscnt += 1
                connectsumtime += (endtime - starttime)
                connectavgtime = connectsumtime / connectsuccesscnt
                if (endtime - starttime) > connectmaxtime:
                    connectmaxtime = endtime - starttime
                if (endtime - starttime) < connectmintime:
                    connectmintime = endtime - starttime
                atLogger.log_timed('Time cost of connect TCP: %ss' % str(endtime - starttime))
                self.assertTrue(atChat.send_command('AT+CIPCLOSE', 40.0))
                self.assertTrue(atChat.has('OK'))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('TCP connect success count: %s' % str(connectsuccesscnt))
        atLogger.log_timed('TCP connect FPY: %s' % (str(connectsuccesscnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of connect TCP is: %ss' % str(connectavgtime))
        atLogger.log_timed('Max time cost of connect TCP is: %ss' % str(connectmaxtime))
        atLogger.log_timed('Min time cost of connect TCP is: %ss' % str(connectmintime))
        self.assertTrue(connectsuccesscnt == testround)

    def test_tcpsidconnect(self):
        disconnectavgtime = 0
        disconnectmaxtime = 0
        disconnectmintime = 1000
        disconnectsumtime = 0
        disconnectsuccesscnt = 0
        testround = 100
        self.assertTrue(atChat.send_command('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send_command('AT+CGDCONT=1,"IP","cmnet"', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send_command('AT+CGACT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            if not atChat.send_command('AT+CIPSTART="TCP","123.57.221.42",6805', 40.0):
                continue
            if not atChat.has('CONNECT OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CIPCLOSE', 40.0)
            endtime = time.time()
            if atChat.has('OK'):
                disconnectsuccesscnt += 1
                disconnectsumtime += (endtime - starttime)
                disconnectavgtime = disconnectsumtime / disconnectsuccesscnt
                if (endtime - starttime) > disconnectmaxtime:
                    disconnectmaxtime = endtime - starttime
                if (endtime - starttime) < disconnectmintime:
                    disconnectmintime = endtime - starttime
                atLogger.log_timed('Time cost of disconnect TCP: %ss' % str(endtime - starttime))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('TCP disconnect success count: %s' % str(disconnectsuccesscnt))
        atLogger.log_timed('TCP disconnect FPY: %s' % (str(disconnectsuccesscnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of disconnect TCP is: %ss' % str(disconnectavgtime))
        atLogger.log_timed('Max time cost of disconnect TCP is: %ss' % str(disconnectmaxtime))
        atLogger.log_timed('Min time cost of disconnect TCP is: %ss' % str(disconnectmintime))
        self.assertTrue(disconnectsuccesscnt == testround)


if __name__=="__main__":
    pass