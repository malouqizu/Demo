#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRSM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRSM - 02 - Set <command> : 176, <fileid> : 28423  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CRSM - 02 - Set <command> : 176, <fileid> : 28423  <<<<<<<<<<')

    def test_CRSM_02(self):
        self.DUT.executeCmd('at+crsm=176,28423,0,0,9', .3)

if __name__ == '__main__':
    unittest.main()