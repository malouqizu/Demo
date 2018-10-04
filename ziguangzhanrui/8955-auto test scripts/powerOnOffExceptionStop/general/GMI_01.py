#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GMI_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GMI - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GMI - 01 - Test command  <<<<<<<<<<')

    def test_GMI_01(self):
        self.DUT.executeCmd('at+gmi=?', .3)

if __name__ == '__main__':
    unittest.main()