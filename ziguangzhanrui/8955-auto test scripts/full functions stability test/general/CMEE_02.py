#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMEE_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMEE - 02 - Set <n> to 0  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at&f', .3)
        self.DUT.executeCmd('at&w', .3)
        print('<<<<<<<<<< CMEE - 02 - Set <n> to 0  <<<<<<<<<<')

    def test_CMEE_02(self):
        self.DUT.executeCmd('at+cmee=0', .3)
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 0')

if __name__ == '__main__':
    unittest.main()