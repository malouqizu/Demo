#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def StabilityTest(TIMES):
    for i in range(0, TIMES):
        n = i + 1
        print('Test Round : ' + str(n)) 
        script = os.getcwd() + r'\runTest.py'
        cmd = 'python ' + script
        os.system(cmd)
        print('\n')

if __name__ == '__main__':
    StabilityTest(1000)
    os.system('pause')

    