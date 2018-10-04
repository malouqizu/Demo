#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMUT_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMUT - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMUT - 01 - Test, read command  <<<<<<<<<<')

    def test_CMUT_01(self):
        self.DUT.executeCmd('at+cmut=?', .3, '+CMUT: (0,1)')
        self.DUT.executeCmd('at+cmut?', .3, '+CMUT: 0')

if __name__ == '__main__':
    unittest.main()