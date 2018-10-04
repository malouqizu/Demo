#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLVL_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLVL - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLVL - 01 - Test, read command  <<<<<<<<<<')

    def test_CLVL_01(self):
        self.DUT.executeCmd('at+clvl=?', .3, '+CLVL: (5-8)')
        self.DUT.executeCmd('at+clvl?', .3, '+CLVL: 6')

if __name__ == '__main__':
    unittest.main()