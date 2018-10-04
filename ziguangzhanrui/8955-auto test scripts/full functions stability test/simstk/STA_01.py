#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class STA_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^STA - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^STA - 01 - Test, read command  <<<<<<<<<<')

    def test_STA_01(self):
        self.DUT.executeCmd('at^sta=?', .3, '^STA: (0,1)')
        self.DUT.executeCmd('at^sta?', .3)

if __name__ == '__main__':
    unittest.main()