#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class EGMR_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> EGMR - 03 - Set <mode> to 2: read mode  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< EGMR - 03 - Set <mode> to 2: read mode  <<<<<<<<<<')

    def test_EGMR_03(self):
        self.DUT.executeCmd('at+egmr=2,7', .3, '+EGMR:012345678901234')

if __name__ == '__main__':
    unittest.main()