#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class STGI_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^STGI - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^STGI - 01 - Test, read command  <<<<<<<<<<')

    def test_STGI_01(self):
        self.DUT.executeCmd('at^stgi=?', .3, '^STGI: (16,19,33,35,36,37,38,211)')
        self.DUT.executeCmd('at^stgi?', .3)

if __name__ == '__main__':
    unittest.main()