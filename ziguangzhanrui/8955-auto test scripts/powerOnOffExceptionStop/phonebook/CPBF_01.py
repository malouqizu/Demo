#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBF_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBF - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBF - 01 - Test command  <<<<<<<<<<')

    def test_CPBF_01(self):
        self.DUT.executeCmd('at+cpbf=?', .3)

if __name__ == '__main__':
    unittest.main()