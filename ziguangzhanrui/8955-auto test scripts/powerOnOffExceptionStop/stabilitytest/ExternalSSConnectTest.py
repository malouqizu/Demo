#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from comm.atc import atLogger, atConfig, pppCtrl, sockCtrl, netCtrl
import time
import random

def random_str(length):
    """ Generate a random string with specified length """
    ret = ''
    pat = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    pat_len = len(pat) - 1
    for i in range(length):
        ret += pat[random.randint(0, pat_len)]
    return ret

def shortshort():
    recv_timeout = 30.0
    ppp_fail_cnt = 0
    tcp_fail_cnt = 0
    successcnt = 0
    testround = 50
    
    for i in range(testround):
        atLogger.case_log('----------------Test Round: %d---------------------' % (i+1))
        if ppp_fail_cnt >= 3 or tcp_fail_cnt >=3:
            atLogger.case_log('Ppp or tcp fail count is more than 3. Test finish!')
            return
        
        atLogger.case_log('PPP dial up...')
        res = pppCtrl.dialup(atConfig.entry_name)
        atLogger.case_log(res['msg'])
        if not res['reValue']:
            ppp_fail_cnt += 1
            atLogger.case_log('------')
            atLogger.case_log('--Total: %d' % (i+1))
            atLogger.case_log('--Pass count: %d' % successcnt)
            continue
        ppp_fail_cnt = 0

        atLogger.case_log('Set route and net...')
        if netCtrl.set_route(atConfig.echo_server) == False or netCtrl.reset_localconn() == False:
            pppCtrl.disconnect(atConfig.entry_name)
            atLogger.case_log('------')
            atLogger.case_log('--Total: %d' % (i+1))
            atLogger.case_log('--Pass count: %d' % successcnt)
            continue
        
        atLogger.case_log('Connect to host...')
        if sockCtrl.connect_host() != 0:
            atLogger.case_log('Fail to connect to host!')
            pppCtrl.disconnect(atConfig.entry_name)
            tcp_fail_cnt += 1
            atLogger.case_log('------')
            atLogger.case_log('--Total: %d' % (i+1))
            atLogger.case_log('--Pass count: %d' % successcnt)
            continue
        tcp_fail_cnt = 0
        
        atLogger.case_log('Send data to host...')
        strlen = random.randint(1, 2048)
        randstr = random_str(strlen)
        sendlen = sockCtrl.send_data(randstr)
        if sendlen != strlen:
            sockCtrl.disconnect_host()
            pppCtrl.disconnect(atConfig.entry_name)
            atLogger.case_log('Fail to send correct data to host!')
            atLogger.case_log('------')
            atLogger.case_log('--Total: %d' % (i+1))
            atLogger.case_log('--Pass count: %d' % successcnt)
            continue
        
        atLogger.case_log('Recieve data from host...')
        recvres = sockCtrl.recv_data(strlen, recv_timeout)
        if recvres != randstr:
            sockCtrl.disconnect_host()
            pppCtrl.disconnect(atConfig.entry_name)
            atLogger.case_log('Recieve wrong data from host!')
            atLogger.case_log('------')
            atLogger.case_log('--Total: %d' % (i+1))
            atLogger.case_log('--Pass count: %d' % successcnt)
            continue
        
        atLogger.case_log('Disconnect from host...')
        sockCtrl.disconnect_host()

        atLogger.case_log('PPP hangup...')
        pppCtrl.disconnect(atConfig.entry_name)

        successcnt += 1
        atLogger.case_log('------')
        atLogger.case_log('--Total: %d' % (i+1))
        atLogger.case_log('--Pass count: %d' % successcnt)


if __name__ == '__main__':
    shortshort()



