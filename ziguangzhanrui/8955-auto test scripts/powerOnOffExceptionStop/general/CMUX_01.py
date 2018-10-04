#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMUX_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMUX - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMUX - 01 - Test, read command  <<<<<<<<<<')

    def test_CMUX_01(self):
        self.DUT.executeCmd('at+cmux=?', .3, '+CMUX: (0)')
        self.DUT.executeCmd('at+cmux?', .3, '+CMUX: 0')

if __name__ == '__main__':
    unittest.main()