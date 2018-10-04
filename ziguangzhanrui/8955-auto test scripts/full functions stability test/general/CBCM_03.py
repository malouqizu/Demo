#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CBCM_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CBCM - 03 - Set <bNumber> to 0  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CBCM - 03 - Set <bNumber> to 0  <<<<<<<<<<')

    def test_CBCM_03(self):
        self.DUT.executeCmd('at+cbcm=0', .3)
        self.DUT.executeCmd('at+cbcm?', .3, '+CBCM:0')

if __name__ == '__main__':
    unittest.main()