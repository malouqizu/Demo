#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CALD_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CALD - 01 - Test, read command  >>>>>>>>>>')
        self.DUT.executeCmd('at+cala="17/12/20,15:05:00",1,0,"a1"', .3)

    def tearDown(self):
        print('<<<<<<<<<< CALD - 01 - Test, read command  <<<<<<<<<<')

    def test_CALD_01(self):
        self.DUT.executeCmd('at+cald=?', .3, '+CALD: 1')

if __name__ == '__main__':
    unittest.main()