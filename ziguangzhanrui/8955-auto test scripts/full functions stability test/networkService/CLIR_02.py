#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLIR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLIR - 02 - Set <n> to 1 : CLIR / OIR invocation  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+clir=0', .3)
        print('<<<<<<<<<< CLIR - 02 - Set <n> to 1 : CLIR / OIR invocation <<<<<<<<<<')

    def test_CLIR_02(self):
        self.DUT.executeCmd('at+clir=1', .3)
        self.DUT.executeCmd('at+clir?', 1.5, '+CLIR:1,0')

if __name__ == '__main__':
    unittest.main()
