#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGATT_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGATT - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGATT - 01 - Test, read command  <<<<<<<<<<')

    def test_CGATT_01(self):
        self.DUT.executeCmd('at+cgatt=?', .3)
        self.DUT.executeCmd('at+cgatt?', 1)

if __name__ == '__main__':
    unittest.main()