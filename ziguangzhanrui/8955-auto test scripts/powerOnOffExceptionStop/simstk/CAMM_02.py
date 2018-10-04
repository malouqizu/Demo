#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CAMM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CAMM - 02 - Set <acmmax>  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+camm="000000","2345"', .3)
        print('<<<<<<<<<< CAMM - 02 - Set <acmmax>  <<<<<<<<<<')

    def test_CAMM_02(self):
        self.DUT.executeCmd('at+camm="00001E","2345"', .3)
        self.DUT.executeCmd('at+camm?', .3, '+CAMM:"00001E"')

if __name__ == '__main__':
    unittest.main()