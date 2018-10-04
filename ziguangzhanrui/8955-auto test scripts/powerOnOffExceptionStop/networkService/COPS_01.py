#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COPS_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>>  COPS - 01 - Test, read command >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  COPS - 01 - Test, read command <<<<<<<<<<')

    def test_COPS_01(self):
        self.DUT.executeCmd('at+cops=?', 15)
        self.DUT.executeCmd('at+cops?', 3)

if __name__ == '__main__':
    unittest.main()