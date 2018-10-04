#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPINC_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^CPINC - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^CPINC - 01 - Test command  <<<<<<<<<<')

    def test_CPINC_01(self):
        self.DUT.executeCmd('at^cpinc=?', .3, '^CPINC: PIN1&PIN2: (1-3), PUK1&PUK2: (1-10)')

if __name__ == '__main__':
    unittest.main()