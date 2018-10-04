#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class 	CAUDIO_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CAUDIO - 02 - Set <n> to 1 : Open audio   >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CAUDIO - 02 - Set <n> to 1 : Open audio  <<<<<<<<<<')

    def test_caudio_02(self):
        self.DUT.executeCmd('at+caudio=1', .3)
        
if __name__ == '__main__':
    unittest.main()