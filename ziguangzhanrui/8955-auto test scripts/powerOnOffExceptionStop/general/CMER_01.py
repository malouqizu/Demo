#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMER_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMER - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMER - 01 - Test, read command  <<<<<<<<<<')

    def test_CMER_01(self):
        self.DUT.executeCmd('at+cmer=?', .3, '+CMER: (3),(0),(0),(0,2)')
        self.DUT.executeCmd('at+cmer?', .3, '+CMER: 3,0,0,0')

if __name__ == '__main__':
    unittest.main()