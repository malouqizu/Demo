#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class 	CAUDIO_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CAUDIO - 03 - Set <n> to 1 : Close audio    >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CAUDIO - 03 - Set <n> to 1 : Close audio   <<<<<<<<<<')

    def test_caudio_03(self):
        self.DUT.executeCmd('at+caudio=0', .3)
        
if __name__ == '__main__':
    unittest.main()