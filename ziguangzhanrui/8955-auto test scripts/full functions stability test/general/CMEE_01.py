#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMEE_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMEE - 01 - Test, read command  >>>>>>>>>>')
        self.DUT.executeCmd('at&f', .3)
        self.DUT.executeCmd('at&w', .3)

    def tearDown(self):
        print('<<<<<<<<<< CMEE - 01 - Test, read command  <<<<<<<<<<')

    def test_CMEE_01(self):
        self.DUT.executeCmd('at+cmee=?', .3, '+CMEE: (0-2)')
        self.DUT.executeCmd('at+cmee?', .3, '+CMEE: 1')

if __name__ == '__main__':
    unittest.main()