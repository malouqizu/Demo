#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import random
from comm.atc import atLogger, atChat, atConfig, relayCtrl


def random_str(length):
    """ Generate a random string with specified length """
    ret = ''
    pat = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    pat_len = len(pat) - 1
    for i in range(length):
        ret += pat[random.randint(0, pat_len)]
    return ret


class CustomerBuildInConnect(unittest.TestCase):
    """test case"""
    name = "Customer Build In Connect"
    use_relay = False
    auto_att = True
    timeout_init_wait = 90.0
    timeout_cgatt = 30.0
    timeout_cgact = 30.0
    timeout_ip = 100.0
    timeout_cpof = 30.0
    timeout_cmd = 1.0
    echo_len = 600

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def supershort(self):
        res = {'pass': False,
               'reg': -1.0,
               'att': -1.0,
               'act': -1.0,
               'tcp': -1.0,
               'csq': -1}

        if self.use_relay:
            time.sleep(3.0)
            relayCtrl.close_channel()
            atChat.reopen()
            time.sleep(1.0)
            relayCtrl.open_channel()
        else:
            if not atChat.send_ok('AT+CPOF', self.timeout_cpof) and \
                    not atChat.send_ok('AT+CPOF', self.timeout_cpof) and \
                    not atChat.send_ok('AT+CPOF', self.timeout_cpof):
                return res
            atChat.reopen()

        if self.auto_att:
            if not atChat.wait('+CGREG: 1', self.timeout_cgatt):
                return res
            res['csq'] = atChat.get_csq()
        else:
            if not atChat.wait('+CREG: 1', self.timeout_init_wait):
                res['csq'] = atChat.get_csq()
                return res
            res['reg'] = atChat.get_uptime()
            res['csq'] = atChat.get_csq()
            if not atChat.send_ok('AT+CGATT=1', self.timeout_cgatt):
                return res
        res['att'] = atChat.get_uptime()

        if not atChat.send_ok('AT+COPS?', self.timeout_cmd):
            return res

        if atChat.contain('46001') or atChat.contain('46009'):
            apn = '3gnet'
        elif atChat.contain('46000') or atChat.contain('46002') or \
                atChat.contain('46007') or atChat.contain('46008'):
            apn = 'cmnet'
        else:
            return res

        starttime = atChat.get_uptime()
        if not atChat.send_ok('AT+CGDCONT=1,"IP","%s"' % (apn), self.timeout_cmd) or \
                not atChat.send_ok('AT+CGACT=1', self.timeout_cgact):
            return res
        res['act'] = atChat.get_uptime() - starttime

        randstr = random_str(self.echo_len)
        starttime = atChat.get_uptime()
        if not atChat.send_ok('AT+CIPSTART="TCP","%s",%d' %
                              (atConfig.echo_server, atConfig.echo_port), self.timeout_ip) or \
                not atChat.wait('CONNECT OK', self.timeout_ip) or \
                not atChat.send('AT+CIPSEND', self.timeout_ip) or \
                not atChat.send(randstr + chr(26), self.timeout_ip) or \
                not atChat.wait(randstr, self.timeout_ip):
            return res 
        res['tcp'] = atChat.get_uptime() - starttime

        """ Before there are methods to make sure socket is closed,
            the sleep is needed.
        """
        if not atChat.send_ok('AT+CIPCLOSE', self.timeout_ip) or \
                not atChat.sleep(5.0) or \
                not atChat.send_ok('AT+CGACT=0', self.timeout_cgact) or \
                not atChat.send_ok('AT+CGATT=0', self.timeout_cgatt):
            return res

        res['pass'] = True
        return res

    def test_supershort(self):
        """ Test for super short TCP socket """
        reg_time_cnts = [0, 0, 0, 0, 0, 0]
        att_time_cnts = [0, 0, 0, 0, 0, 0]
        act_time_cnts = [0, 0, 0, 0]
        tcp_time_cnts = [0, 0, 0, 0, 0]
        reg_total = 0.0
        att_total = 0.0
        act_total = 0.0
        tcp_total = 0.0
        reg_cnt = 0
        att_cnt = 0
        act_cnt = 0
        tcp_cnt = 0
        fail_cnt = 0
        pass_cnt = 0
        csq_min = -1
        csq_max = -1

        for i in range(1000):
            atLogger.case_timed_log('Test Round: %d' % (i + 1))
            res = self.supershort()
            if not res['pass']:
                fail_cnt += 1
            else:
                pass_cnt += 1

            csq = res['csq']
            if csq > 0:
                if csq_min < 0 or csq < csq_min:
                    csq_min = csq
                if csq_max < 0 or csq > csq_max:
                    csq_max = csq

            reg_time = res['reg']
            if reg_time > 0:
                reg_cnt += 1
                reg_total += reg_time
                idx = 0 if reg_time < 12 \
                    else 1 if reg_time < 15 \
                    else 2 if reg_time < 20 \
                    else 3 if reg_time < 25 \
                    else 4
                reg_time_cnts[idx] += 1
            else:
                reg_time_cnts[5] += 1

            att_time = res['att']
            if att_time > 0:
                att_cnt += 1
                att_total += att_time
                idx = 0 if att_time < 12 \
                    else 1 if att_time < 15 \
                    else 2 if att_time < 20 \
                    else 3 if att_time < 25 \
                    else 4
                att_time_cnts[idx] += 1
            else:
                att_time_cnts[5] += 1

            act_time = res['act']
            if act_time > 0:
                act_cnt += 1
                act_total += act_time
                idx = 0 if act_time < 1 \
                    else 1 if act_time < 3 \
                    else 2
                act_time_cnts[idx] += 1
            else:
                act_time_cnts[3] += 1

            tcp_time = res['tcp']
            if tcp_time > 0:
                tcp_cnt += 1
                tcp_total += tcp_time
                idx = 0 if tcp_time < 3 \
                    else 1 if tcp_time < 6 \
                    else 2 if tcp_time < 10 \
                    else 3
                tcp_time_cnts[idx] += 1
            else:
                tcp_time_cnts[4] += 1

            atLogger.case_log('CSQ: %d' % (csq))
            atLogger.case_log('Time of register: %.2fs' % (reg_time))
            atLogger.case_log('Time of attach: %.2fs' % (att_time))
            atLogger.case_log('Time of active: %.2fs' % (act_time))
            atLogger.case_log('Time of TCP: %.2fs' % (tcp_time))
            atLogger.case_log('Total round: %d (%d:%d)' %
                              (pass_cnt + fail_cnt, pass_cnt, fail_cnt))
            atLogger.case_log('Register time dist (<12, 12~15, 15~20, 20~25, >25): %d %d %d %d %d (%d)' %
                              (reg_time_cnts[0], reg_time_cnts[1], reg_time_cnts[2],
                               reg_time_cnts[3], reg_time_cnts[4], reg_time_cnts[5]))
            atLogger.case_log('Attach time dist (<12, 12~15, 15~20, 20~25, >25): %d %d %d %d %d (%d)' %
                              (att_time_cnts[0], att_time_cnts[1], att_time_cnts[2],
                               att_time_cnts[3], att_time_cnts[4], att_time_cnts[5]))
            atLogger.case_log('Active time dist (<1, 1~3, >3): %d %d %d (%d)' %
                              (act_time_cnts[0], act_time_cnts[1], act_time_cnts[2], act_time_cnts[3]))
            atLogger.case_log('TCP time dist (<3, 3~6, 6~10, >10): %d %d %d %d (%d)' %
                              (tcp_time_cnts[0], tcp_time_cnts[1], tcp_time_cnts[2],
                               tcp_time_cnts[3], tcp_time_cnts[4]))

        reg_avg = -1 if reg_cnt == 0 else reg_total / reg_cnt
        att_avg = -1 if att_cnt == 0 else att_total / att_cnt
        act_avg = -1 if act_cnt == 0 else act_total / act_cnt
        tcp_avg = -1 if tcp_cnt == 0 else tcp_total / tcp_cnt

        atLogger.case_log('')
        atLogger.case_log('CSQ range: %d - %d' % (csq_min, csq_max))
        atLogger.case_log('Average time of register: %.2fs' % (reg_avg))
        atLogger.case_log('Average time of attach: %.2fs' % (att_avg))
        atLogger.case_log('Average time of active: %.2fs' % (act_avg))
        atLogger.case_log('Average time of TCP: %.2fs' % (tcp_avg))
        self.assertTrue(fail_cnt == 0)

    @unittest.skip('')
    def test_customershort(self):
        successcnt = 0
        testround = 100
        testtime = 0
        self.assertTrue(atChat.send('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGDCONT=1,"IP","cmnet"', 40.0))
        self.assertTrue(atChat.has('OK'))
        for i in range(testround):
            atLogger.case_log(
                '------------Test Round: %s ---------' % str(i + 1))
            testtime = 0
            if not atChat.send('AT+CGACT=1', 40.0):
                continue
            if not atChat.has('OK'):
                continue
            if not atChat.send('AT+CIPSTART="TCP","123.57.221.42",6805', 120.0):
                continue
            if not atChat.has('CONNECT OK'):
                continue
            if not atChat.send('AT+CIPSEND', 10.0):
                atChat.send('AT+CIPCLOSE', 30.0)
                continue
            randstr = random_str(600)
            if not atChat.send(randstr + chr(26), 10.0):
                atChat.send('AT+CIPCLOSE', 30.0)
                continue
            if not atChat.wait(randstr, 40.0):
                atChat.send('AT+CIPCLOSE', 30.0)
                continue
            if not atChat.send('AT+CIPCLOSE', 30.0):
                continue
            if not atChat.has('OK'):
                continue
            if not atChat.send('AT+CGACT=0', 40.0):
                continue
            if not atChat.has('OK'):
                continue
            successcnt += 1
            atLogger.case_log('Total test round: %s' % str(i + 1))
            atLogger.case_log('Success count: %s' % str(successcnt))
        self.assertTrue(successcnt == testround)

    @unittest.skip('')
    def test_customerlong(self):
        successcnt = 0
        testround = 100
        recvavgtime = 0
        recvmaxtime = 0
        recvmintime = 1000
        recvsumtime = 0
        self.assertTrue(atChat.send('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGDCONT=1,"IP","cmnet"', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGACT=1', 40.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send(
            'AT+CIPSTART="TCP","123.57.221.42",6800', 120.0))
        self.assertTrue(atChat.has('CONNECT OK'))
        for i in range(testround):
            atLogger.case_log(
                '-----------Test Round: %s ----------' % str(i + 1))
            randstr = random_str(600)
            if not atChat.send('AT+CIPSEND', 10.0):
                if not atChat.send("\r\n", 10.0):
                    continue
            starttime = time.time()
            if not atChat.send(randstr + chr(26), 10.0):
                continue
            if not atChat.has('OK'):
                continue
            if not atChat.wait(randstr, 40.0):
                continue
            endtime = time.time()
            successcnt += 1
            recvsumtime += (endtime - starttime)
            recvavgtime = recvsumtime / (i + 1)
            if (endtime - starttime) > recvmaxtime:
                recvmaxtime = (endtime - starttime)
            if (endtime - starttime) < recvmintime:
                recvmintime = (endtime - starttime)
            atLogger.case_log('Time from sending to receiving: %ss' %
                              str(endtime - starttime))
            atLogger.case_log('Total test round: %s' % str(i + 1))
            atLogger.case_log('Success count: %s' % str(successcnt))
            atLogger.case_log('Fail count: %s' % str(i + 1 - successcnt))
            time.sleep(30.0)
        self.assertTrue(atChat.send('AT+CIPCLOSE', 30.0))
        self.assertTrue(atChat.has('OK'))
        self.assertTrue(atChat.send('AT+CGACT=0', 40.0))
        self.assertTrue(atChat.has('OK'))
        atLogger.case_log(
            '====================================================')
        atLogger.case_log('Total test round: %s' % str(testround))
        atLogger.case_log('Success count: %s' % str(successcnt))
        atLogger.case_log('FPY: %s' %
                          (str(successcnt / testround * 100) + '%'))
        atLogger.case_log(
            'Average time cost of send & receive data is: %ss' % str(recvavgtime))
        atLogger.case_log(
            'Max time cost of send & receive data is: %ss' % str(recvmaxtime))
        atLogger.case_log(
            'Min time cost of send & receive data is: %ss' % str(recvmintime))
        self.assertTrue(successcnt == testround)

if __name__ == '__main__':
    unittest.main()
