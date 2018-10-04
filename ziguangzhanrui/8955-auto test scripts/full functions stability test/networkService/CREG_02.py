#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CREG_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CREG - 02 - Set <n> to 0  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+creg=1', .3)
        print('<<<<<<<<<< CREG - 02 - Set <n> to 0  <<<<<<<<<<')

    def test_creg_02(self):
        self.DUT.executeCmd('at+creg=0', .3)
        self.DUT.executeCmd('at+creg?', .3, '+CREG: 0,1')

if __name__ == '__main__':
    unittest.main()