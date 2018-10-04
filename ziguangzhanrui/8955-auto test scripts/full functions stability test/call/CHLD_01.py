#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CHLD_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CHLD - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CHLD - 01 - Test command  <<<<<<<<<<')

    def test_chld_01(self):
        self.DUT.executeCmd('at+chld=?', .3, '+CHLD: (0,1,1X,2,2X,3)')

if __name__ == '__main__':
    unittest.main()