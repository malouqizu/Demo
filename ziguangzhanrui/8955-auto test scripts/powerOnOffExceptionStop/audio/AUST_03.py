#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class AUST_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> AUST - 03 - Set <value> to 2  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  AUST - 03 - Set <value> to 2 <<<<<<<<<<')

    def test_AUST_03(self):
        self.DUT.executeCmd('at+aust=2', 3)
        self.DUT.executeCmd('at+aust', 3)
        self.DUT.executeCmd('at+auend', 3)

if __name__ == '__main__':
    unittest.main()