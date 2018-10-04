#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GMR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GMR - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GMR - 01 - Test command  <<<<<<<<<<')

    def test_GMR_01(self):
        self.DUT.executeCmd('at+gmr=?', .3)

if __name__ == '__main__':
    unittest.main()