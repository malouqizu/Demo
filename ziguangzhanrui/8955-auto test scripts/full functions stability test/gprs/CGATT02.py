#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGATT_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGATT - 02 - Set <value> to 1 : attached  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGATT - 02 - Set <value> to 1 : attached  <<<<<<<<<<')

    def test_CGATT_02(self):
        self.DUT.executeCmd('at+cgatt=1', 5)
        self.DUT.executeCmd('at+cgatt?', 1)

if __name__ == '__main__':
    unittest.main()