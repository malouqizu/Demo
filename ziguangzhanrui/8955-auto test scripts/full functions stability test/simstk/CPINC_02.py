#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPINC_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^CPINC - 02 - AT^CPINC  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^CPINC - 02 - AT^CPINC  <<<<<<<<<<')

    def test_CPINC_02(self):
        self.DUT.executeCmd('at^cpinc', .3, '^CPINC:3,10,3,10')

if __name__ == '__main__':
    unittest.main()