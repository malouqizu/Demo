#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRSM_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRSM - 03 - Set <command> : 176, <fileid> : 28481  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CRSM - 03 - Set <command> : 176, <fileid> : 28481  <<<<<<<<<<')

    def test_CRSM_03(self):
        self.DUT.executeCmd('at+crsm=176,28481,0,0,5', .3)

if __name__ == '__main__':
    unittest.main()