#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSSN_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSSN - 03 - Set <n> to 0: disable, <m> to 0: disable  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSSN - 03 - Set <n> to 0: disable, <m> to 0: disable <<<<<<<<<<')

    def test_CSSN_03(self):
        self.DUT.executeCmd('at+cssn=0,0', .3)
        self.DUT.executeCmd('at+cssn?', .3, '+CSSN:0,0')

if __name__ == '__main__':
    unittest.main()
