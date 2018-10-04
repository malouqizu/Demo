#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CBCM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CBCM - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CBCM - 01 - Test, read command  <<<<<<<<<<')

    def test_CBCM_01(self):
        self.DUT.executeCmd('at+cbcm=?', .3, '+CBCM: (0-1)')
        self.DUT.executeCmd('at+cbcm?', .3, '+CBCM:0')

if __name__ == '__main__':
    unittest.main()