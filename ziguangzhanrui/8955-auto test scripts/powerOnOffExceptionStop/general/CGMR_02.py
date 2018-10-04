#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGMR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGMR - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGMR - 02 - Execute command  <<<<<<<<<<')

    def test_CGMR_02(self):
        self.DUT.executeCmd('at+cgmr', .3, '20120707')

if __name__ == '__main__':
    unittest.main()