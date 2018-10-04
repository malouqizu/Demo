#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CALD_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CALD - 02 - Delete alarm <n>  >>>>>>>>>>')
        self.DUT.executeCmd('at+cala="17/12/20,15:05:00",1,0,"a1"', .3)

    def tearDown(self):
        print('<<<<<<<<<< CALD - 02 - Delete alarm <n>  <<<<<<<<<<')

    def test_CALD_02(self):
        self.DUT.executeCmd('at+cald=1', .3)

if __name__ == '__main__':
    unittest.main()