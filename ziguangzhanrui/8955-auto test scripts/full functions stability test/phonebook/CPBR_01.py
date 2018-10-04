#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBR - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBR - 01 - Test command  <<<<<<<<<<')

    def test_CPBR_01(self):
        self.DUT.executeCmd('at+cpbr=?', .3)

if __name__ == '__main__':
    unittest.main()