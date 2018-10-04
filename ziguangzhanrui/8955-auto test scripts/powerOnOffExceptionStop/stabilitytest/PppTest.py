#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from comm.atc import atLogger, atConfig, pppCtrl, netCtrl
import time
import subprocess
import re


def doping(ip):
    p = subprocess.Popen(["ping.exe", ip], stdin = subprocess.PIPE, stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell = True)
    out = p.stdout.read().decode('gb2312')
    atLogger.case_log(out)
    regex = re.compile(r'\w*%\w*')
    packetLossRateList = regex.findall(out)
    if packetLossRateList[0] == '0%':
        return True
    else:
        return False


def ppptest(entryname, ip):
    atLogger.case_log('PPP dial up...')
    starttime = time.time()
    res = pppCtrl.dialup(entryname)
    atLogger.case_log(res['msg'])
    if res['reValue'] == True:
        ppptime = time.time() - starttime
    else:
        return False, 0, 0
    atLogger.case_log('Set route and net...')
    if netCtrl.set_route(atConfig.ping_addr) == False or netCtrl.reset_localconn() == False:
        starttime = time.time()
        pppCtrl.disconnect(atConfig.entry_name)
        return False, ppptime, time.time()-starttime
    atLogger.case_log('Begin to ping...')
    if not doping(ip):
        starttime = time.time()
        pppCtrl.disconnect(entryname)
        atLogger.case_log('PPP hangup')
        return False, ppptime, time.time()-starttime
    atLogger.case_log('PPP hangup...')
    starttime = time.time()
    pppCtrl.disconnect(entryname)
    ppphanguptime = time.time() - starttime
    return True, ppptime, ppphanguptime


if __name__ == '__main__':
    avg_ppp_time = 0
    ppp_sum_time = 0
    ppp_pass_cnt = 0
    avg_ppphangup_time = 0
    ppphangup_sum_time = 0
    ppphangup_cnt = 0
    successcnt = 0
    testround = 10
    for i in range(testround):
        atLogger.case_log('----------------Test Round: %d---------------------' % (i+1))
        res = ppptest(atConfig.entry_name, atConfig.ping_addr)
        if res[0] == True:
            successcnt += 1
        if res[1] != 0:
            ppp_pass_cnt += 1
            ppp_sum_time += res[1]
            avg_ppp_time = ppp_sum_time/ppp_pass_cnt
        if res[2] != 0:
            ppphangup_cnt += 1
            ppphangup_sum_time += res[2]
            avg_ppphangup_time = ppphangup_sum_time/ppphangup_cnt
        atLogger.case_log('------')
        atLogger.case_log('--Total: %d' % (i+1))
        atLogger.case_log('--Pass count: %d' % successcnt)
        atLogger.case_log('--Average time of PPP dial up: %.2fs' % avg_ppp_time)
        atLogger.case_log('--Average time of PPP hang up: %.2fs' % avg_ppphangup_time)



