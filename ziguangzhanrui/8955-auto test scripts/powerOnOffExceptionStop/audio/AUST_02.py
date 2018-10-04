#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class AUST_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> AUST - 02 - Set <value> to 1 >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  AUST - 02 - Set <value> to 1<<<<<<<<<<')

    def test_AUST_02(self):
        self.DUT.executeCmd('at+aust=1', 3)
        self.DUT.executeCmd('at+aust', 3)
        self.DUT.executeCmd('at+auend', 3)

if __name__ == '__main__':
    unittest.main()