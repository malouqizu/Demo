#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CREG_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CREG - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CREG - 01 - Test, read command  <<<<<<<<<<')

    def test_CREG_01(self):
        self.DUT.executeCmd('at+creg=?', .3, '+CREG: (0-2)')
        self.DUT.executeCmd('at+creg?', .3, '+CREG: 1,1')

if __name__ == '__main__':
    unittest.main()
    