#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class STR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^STR - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^STR - 01 - Test, read command  <<<<<<<<<<')

    def test_STR_01(self):
        self.DUT.executeCmd('at^str=?', .3, '^STR: (16,19,33,35,36,37,38,211,254,255)')
        self.DUT.executeCmd('at^str=?', .3)

if __name__ == '__main__':
    unittest.main()