#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLIR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLIR - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLIR - 01 - Test, read command <<<<<<<<<<')

    def test_CLIR_01(self):
        self.DUT.executeCmd('at+clir=?', 1, '+CLIR:(0-2)')
        self.DUT.executeCmd('at+clir?', 1.5, '+CLIR:0,0')

if __name__ == '__main__':
    unittest.main()
