#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGATT_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGATT - 03 - Set <value> to 0 : dettached  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGATT - 03 - Set <value> to 0 : dettached  <<<<<<<<<<')

    def test_CGATT_03(self):
        self.DUT.executeCmd('at+cgatt=0', 5)
        self.DUT.executeCmd('at+cgatt?', 1)

if __name__ == '__main__':
    unittest.main()