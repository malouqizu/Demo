#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CCLK_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CCLK - 01 - Test, read commad  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CCLK - 01 - Test, read commad  <<<<<<<<<<')

    def test_CCLK_01(self):
        self.DUT.executeCmd('at+cclk=?', .3)
        self.DUT.executeCmd('at+cclk?', .3)

if __name__ == '__main__':
    unittest.main()