#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GMM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GMM - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GMM - 01 - Test command  <<<<<<<<<<')

    def test_GMM_01(self):
        self.DUT.executeCmd('at+gmm=?', .3)

if __name__ == '__main__':
    unittest.main()