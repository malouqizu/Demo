#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBS_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBS - 03 - Set <storge> "ON" : SIM (or MT) own numbers (MSISDNs) list  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBS - 03 - Set <storge> "ON" : SIM (or MT) own numbers (MSISDNs) list  <<<<<<<<<<')

    def test_CPBS_03(self):
        self.DUT.executeCmd('at+cpbs="ON"', 3)
        self.DUT.executeCmd('at+cpbs?', 3)

if __name__ == '__main__':
    unittest.main()