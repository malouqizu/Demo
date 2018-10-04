#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class AUST_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> AUST - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  AUST - 01 - Test command  <<<<<<<<<<')

    def test_AUST_01(self):
        self.DUT.executeCmd('at+aust=?', .3, '+AUST: (0-2)')

if __name__ == '__main__':
    unittest.main()