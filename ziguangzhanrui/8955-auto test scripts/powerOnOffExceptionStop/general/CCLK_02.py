#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CCLK_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CCLK - 02 - Set <time>  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CCLK - 02 - Set <time>  <<<<<<<<<<')

    def test_CCLK_02(self):
        self.DUT.executeCmd('at+cclk="17/12/16,14:47:30+8"', .3)
        self.DUT.executeCmd('at+cclk?', .3, '+CCLK: "17/12/16,14:47:30+8"')

if __name__ == '__main__':
    unittest.main()