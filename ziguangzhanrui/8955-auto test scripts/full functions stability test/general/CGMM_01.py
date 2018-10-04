#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGMM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGMM - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGMM - 01 - Test command  <<<<<<<<<<')

    def test_CGMM_01(self):
        self.DUT.executeCmd('at+cgmm=?', .3)

if __name__ == '__main__':
    unittest.main()