#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSCS_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSCS - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSCS - 01 - Test, read command  <<<<<<<<<<')

    def test_CSCS_01(self):
        self.DUT.executeCmd('at+cscs=?', .3, '+CSCS: ("GSM","HEX","PCCP936","UCS2")')
        self.DUT.executeCmd('at+cscs?', .3, '+CSCS: "PCCP936"')

if __name__ == '__main__':
    unittest.main()