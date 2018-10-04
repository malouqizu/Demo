#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GMI_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GMI - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GMI - 02 - Execute command  <<<<<<<<<<')

    def test_GMI_02(self):
        self.DUT.executeCmd('at+gmi', .3, 'RDA')

if __name__ == '__main__':
    unittest.main()