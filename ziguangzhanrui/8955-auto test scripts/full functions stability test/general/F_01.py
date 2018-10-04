#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class F_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> &F - 01 - AT&F >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< &F - 01 - AT&F <<<<<<<<<<')

    def test_F_01(self):
        self.DUT.executeCmd('at+cmee=2', .3)
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 2')
        self.DUT.executeCmd('at&f', .3)
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 1')

if __name__ == '__main__':
    unittest.main()