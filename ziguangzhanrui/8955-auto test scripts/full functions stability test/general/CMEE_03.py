#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMEE_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMEE - 03 - Set <n> to 1  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at&f', .3)
        self.DUT.executeCmd('at&w', .3)
        print('<<<<<<<<<< CMEE - 03 - Set <n> to 1  <<<<<<<<<<')

    def test_CMEE_03(self):
        self.DUT.executeCmd('at+cmee=1', .3)
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 1')

if __name__ == '__main__':
    unittest.main()