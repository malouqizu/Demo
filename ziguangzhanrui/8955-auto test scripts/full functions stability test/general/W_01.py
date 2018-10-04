#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT
import time

class W_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> &W - 01 - Ignore [<value>]  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at&f', .3)
        self.DUT.executeCmd('at&w', .3)
        print('<<<<<<<<<< &W - 01 - Ignore [<value>]  <<<<<<<<<<')

    def test_W_01(self):
        self.DUT.executeCmd('at+cmee=2', .3)
        self.DUT.executeCmd('at&w', .3,)
        self.DUT.executeCmd('at+cmee=1', .3)
        self.DUT.executeCmd('at+cpof', .3)
        print('...... Reboot DUT, waiting 30s ......')
        time.sleep(30)
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 2')

if __name__ == '__main__':
    unittest.main()