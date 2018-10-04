#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CAUDIO_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CAUDIO - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CAUDIO - 01 - Test command <<<<<<<<<<')

    def test_ccaudio_01(self):
        self.DUT.executeCmd('at+caudio=?', .3, '+CAUDIO: (0-1)')

if __name__ == '__main__':
    unittest.main()