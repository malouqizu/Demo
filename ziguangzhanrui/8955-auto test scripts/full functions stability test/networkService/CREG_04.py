#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CREG_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CREG - 04 - Set <n> to 2  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+creg=1', .3)
        print('<<<<<<<<<< CREG - 04 - Set <n> to 2  <<<<<<<<<<')

    def test_CREG_04(self):
        self.DUT.executeCmd('at+creg=2', .3)
        self.DUT.executeCmd('at+creg?', .3)

if __name__ == '__main__':
    unittest.main()
    