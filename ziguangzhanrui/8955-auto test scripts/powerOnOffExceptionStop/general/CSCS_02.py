#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSCS_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSCS - 02 - Set <chset> to  "GSM"  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSCS - 02 - Set <chset> to  "GSM"  <<<<<<<<<<')

    def test_CSCS_02(self):
        self.DUT.executeCmd('at+cscs="GSM"', 1)
        self.DUT.executeCmd('at+cscs?', .3, '+CSCS: "GSM"')

if __name__ == '__main__':
    unittest.main()