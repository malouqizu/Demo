#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class AUST_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> AUST - 04 - Set <value> to 0  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  AUST - 04 - Set <value> to 0 <<<<<<<<<<')

    def test_AUST_04(self):
        self.DUT.executeCmd('at+aust=0', 3)
        self.DUT.executeCmd('at+aust', 3)
        self.DUT.executeCmd('at+auend', 3)

if __name__ == '__main__':
    unittest.main()