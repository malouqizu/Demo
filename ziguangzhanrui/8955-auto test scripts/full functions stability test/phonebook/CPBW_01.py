#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBW_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBW - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBW - 01 - Test command  <<<<<<<<<<')

    def test_CPBW_01(self):
        self.DUT.executeCmd('at+cpbw=?', .3)

if __name__ == '__main__':
    unittest.main()