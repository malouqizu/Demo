#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from comm.at import AtTest, COMPORT

class D_01(unittest.TestCase):
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> D - 01 - [<dial_string>][;] - Emergency call  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< D - 01 - [<dial_string>][;] - Emergency call  <<<<<<<<<<')

    def test_D_01(self):
        self.DUT.executeCmd('atd112', 2)
        print(' +CIEV: "CALL",1', '\n', '+CIEV: "SOUNDER",1', '\n', 'waiting 30s ......')
        time.sleep(30)
        self.DUT.executeCmd('ath', 1, '+CIEV: "CALL",0')
        time.sleep(6)
        self.DUT.executeCmd('atd911', 2)
        print(' +CIEV: "CALL",1', '\n', '+CIEV: "SOUNDER",1', '\n', 'waiting 30s ......')
        time.sleep(30)
        self.DUT.executeCmd('ath', 1, '+CIEV: "CALL",0')

if __name__ == '__main__':
    unittest.main()
