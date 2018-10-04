#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CBCM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CBCM - 02 - Set <bNumber> to 1  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CBCM - 02 - Set <bNumber> to 1  <<<<<<<<<<')

    def test_CBCM_02(self):
        self.DUT.executeCmd('at+cbcm=1', .3)
        self.DUT.executeCmd('at+cbcm?', .3, '+CBCM:1')

if __name__ == '__main__':
    unittest.main()