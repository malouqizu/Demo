#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGMM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGMM - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGMM - 02 - Execute command  <<<<<<<<<<')

    def test_CGMM_02(self):
        self.DUT.executeCmd('at+cgmm', .3, 'RDA MODULE ID')

if __name__ == '__main__':
    unittest.main()