#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLIR_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLIR - 04 - Set <n> to 0   >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLIR - 04 - Set <n> to 0  <<<<<<<<<<')

    def test_CLIR_04(self):
        self.DUT.executeCmd('at+clir=0', .3)
        self.DUT.executeCmd('at+clir?', 1.5, '+CLIR:0,0')

if __name__ == '__main__':
    unittest.main()
    