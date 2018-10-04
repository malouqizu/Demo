#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPUC_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPUC - 02 - Set <currency>,<ppu>  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPUC - 02 - Set <currency>,<ppu>  <<<<<<<<<<')

    def test_CPUC_02(self):
        self.DUT.executeCmd('at+cpuc="USD","0.144","2345"', .3)
        self.DUT.executeCmd('at+cpuc?', .3, '+CPUC:"USD","0.144"')

if __name__ == '__main__':
    unittest.main()