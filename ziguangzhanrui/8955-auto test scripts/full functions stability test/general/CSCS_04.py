#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSCS_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSCS - 04- Set <chset> to  "UCS2"  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSCS - 04- Set <chset> to  "UCS2"  <<<<<<<<<<')

    def test_CSCS_04(self):
        self.DUT.executeCmd('at+cscs="UCS2"', 1)
        self.DUT.executeCmd('at+cscs?', .3, '+CSCS: "UCS2"')

if __name__ == '__main__':
    unittest.main()