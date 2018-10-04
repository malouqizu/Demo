#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMEE_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMEE - 04 - Set <n> to 2  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at&f', .3)
        self.DUT.executeCmd('at&w', .3)
        print('<<<<<<<<<< CMEE - 04 - Set <n> to 2  <<<<<<<<<<')

    def test_CMEE_03(self):
        self.DUT.executeCmd('at+cmee=2', .3)
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 2')

if __name__ == '__main__':
    unittest.main()