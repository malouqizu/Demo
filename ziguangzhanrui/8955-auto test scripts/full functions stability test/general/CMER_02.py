#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CMER_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CMER - 02 - Set <mode>, <keyp>, <disp>, <ind> to 3, 0, 0, 0  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CMER - 02 - Set <mode>, <keyp>, <disp>, <ind> to 3, 0, 0, 0  <<<<<<<<<<')

    def test_CMER_02(self):
        self.DUT.executeCmd('at+cmer=3,0,0,0', .3)
        self.DUT.executeCmd('at+cmer?', .3, '+CMER: 3,0,0,0')

if __name__ == '__main__':
    unittest.main()