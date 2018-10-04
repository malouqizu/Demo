#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSSN_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSSN - 02 - Set <n> to 1: enable, <m> to 1: enable  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+cssn=0,0', .3)
        print('<<<<<<<<<< CSSN - 02 - Set <n> to 1: enable, <m> to 1: enable <<<<<<<<<<')

    def test_CSSN_02(self):
        self.DUT.executeCmd('at+cssn=1,1', .3)
        self.DUT.executeCmd('at+cssn?', .3, '+CSSN:1,1')

if __name__ == '__main__':
    unittest.main()