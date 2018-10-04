#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSCS_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSCS - 03- Set <chset> to  "HEX"  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSCS - 03- Set <chset> to  "HEX"  <<<<<<<<<<')

    def test_CSCS_03(self):
        self.DUT.executeCmd('at+cscs="HEX"', 1)
        self.DUT.executeCmd('at+cscs?', .3, '+CSCS: "HEX"')

if __name__ == '__main__':
    unittest.main()