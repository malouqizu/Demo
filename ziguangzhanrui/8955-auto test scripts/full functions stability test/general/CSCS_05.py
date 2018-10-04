#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSCS_05(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSCS - 05- Set <chset> to  "PCCP936"  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSCS - 05- Set <chset> to  "PCCP936"  <<<<<<<<<<')

    def test_CSCS_05(self):
        self.DUT.executeCmd('at+cscs="PCCP936"', 1)
        self.DUT.executeCmd('at+cscs?', .3, '+CSCS: "PCCP936"')

if __name__ == '__main__':
    unittest.main()