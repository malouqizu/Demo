#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLIR_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLIR - 03 - Set <n> to 2 : CLIR / OIR suppression  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+clir=0', .3)
        print('<<<<<<<<<< CLIR - 03 - Set <n> to 2 : CLIR / OIR suppression <<<<<<<<<<')

    def test_CLIR_03(self):
        self.DUT.executeCmd('at+clir=2', .3)
        self.DUT.executeCmd('at+clir?', 1.5, '+CLIR:2,0')

if __name__ == '__main__':
    unittest.main()
    