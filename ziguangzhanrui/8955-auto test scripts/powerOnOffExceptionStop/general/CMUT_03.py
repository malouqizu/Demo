#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMUT_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMUT - 03 - Set <n> to 0: mute off  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMUT - 03 - Set <n> to 0: mute off  <<<<<<<<<<')

    def test_CMUT_03(self):
        self.DUT.executeCmd('at+cmut=0', .3)
        self.DUT.executeCmd('at+cmut?', .3, '+CMUT: 0')

if __name__ == '__main__':
    unittest.main()