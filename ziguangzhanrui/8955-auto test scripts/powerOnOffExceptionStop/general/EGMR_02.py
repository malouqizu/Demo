#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class EGMR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> EGMR - 02 - Set <mode> to 1: write mode  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< EGMR - 02 - Set <mode> to 1: write mode  <<<<<<<<<<')

    def test_EGMR_02(self):
        self.DUT.executeCmd('at+egmr=1,7,"012345678901234"', .3)

if __name__ == '__main__':
    unittest.main()