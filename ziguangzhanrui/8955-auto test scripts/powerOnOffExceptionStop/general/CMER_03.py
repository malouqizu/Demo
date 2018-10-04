#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMER_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMER - 03 - Set <mode>, <keyp>, <disp>, <ind> to 3, 0, 0, 2  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMER - 03 - Set <mode>, <keyp>, <disp>, <ind> to 3, 0, 0, 2  <<<<<<<<<<')

    def test_CMER_03(self):
        self.DUT.executeCmd('at+cmer=3,0,0,2', .3)
        self.DUT.executeCmd('at+cmer?', .3, '+CMER: 3,0,0,2')

if __name__ == '__main__':
    unittest.main()