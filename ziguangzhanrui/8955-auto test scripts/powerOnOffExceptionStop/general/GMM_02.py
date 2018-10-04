#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GMM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GMM - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GMM - 02 - Execute command  <<<<<<<<<<')

    def test_GMM_02(self):
        self.DUT.executeCmd('at+gmm', .3, 'RDA MODULE ID')

if __name__ == '__main__':
    unittest.main()