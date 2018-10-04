#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBS_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBS - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBS - 01 - Test, read command  <<<<<<<<<<')

    def test_CPBS_01(self):
        self.DUT.executeCmd('at+cpbs=?', .3, '+CPBS: ("SM","ON","FD","LD")')
        self.DUT.executeCmd('at+cpbs?', 3)

if __name__ == '__main__':
    unittest.main()