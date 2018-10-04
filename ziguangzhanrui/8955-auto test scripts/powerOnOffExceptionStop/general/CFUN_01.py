#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CFUN_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CFUN - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CFUN - 01 - Test, read command  <<<<<<<<<<')

    def test_CFUN_01(self):
        self.DUT.executeCmd('at+cfun=?', .3, '+CFUN: (0,1)')
        self.DUT.executeCmd('at+cfun?', .3, '+CFUN: 1')

if __name__ == '__main__':
    unittest.main()