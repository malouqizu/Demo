#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLCC_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLCC - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLCC - 01 - Test command  <<<<<<<<<<')

    def test_clcc_01(self):
        self.DUT.executeCmd('at+clcc=?', .3)

if __name__ == '__main__':
    unittest.main()