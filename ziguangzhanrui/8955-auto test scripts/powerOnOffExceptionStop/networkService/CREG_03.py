#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CREG_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CREG - 03 - Set <n> to 1  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CREG - 03 - Set <n> to 1  <<<<<<<<<<')

    def test_CREG_03(self):
        self.DUT.executeCmd('at+creg=1', .3)
        self.DUT.executeCmd('at+creg?', .3, '+CREG: 1,1')

if __name__ == '__main__':
    unittest.main()
    