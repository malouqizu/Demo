#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CAMM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CAMM - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CAMM - 01 - Test, read command  <<<<<<<<<<')

    def test_CAMM_01(self):
        self.DUT.executeCmd('at+camm=?', .3)
        self.DUT.executeCmd('at+camm?', .3, '+CAMM:"000000"')

if __name__ == '__main__':
    unittest.main()