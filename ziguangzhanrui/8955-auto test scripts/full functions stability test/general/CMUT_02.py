#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMUT_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMUT - 02 - Set <n> to 1: mute on  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMUT - 02 - Set <n> to 1: mute on  <<<<<<<<<<')

    def test_CMUT_02(self):
        self.DUT.executeCmd('at+cmut=1', .3)
        self.DUT.executeCmd('at+cmut?', .3, '+CMUT: 1')

if __name__ == '__main__':
    unittest.main()