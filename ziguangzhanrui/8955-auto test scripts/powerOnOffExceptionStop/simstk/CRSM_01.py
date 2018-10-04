#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRSM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRSM - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CRSM - 01 - Test command  <<<<<<<<<<')

    def test_CRSM_01(self):
        self.DUT.executeCmd('at+crsm=?', .3)

if __name__ == '__main__':
    unittest.main()