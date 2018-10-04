#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLVL_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLVL -02 - Set <level> to 5, 7, 8, 6  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLVL -02 - Set <level> to 5, 7, 8, 6  <<<<<<<<<<')

    def test_CLVL_02(self):
        self.DUT.executeCmd('at+clvl=5', .3)
        self.DUT.executeCmd('at+clvl=7', .3)
        self.DUT.executeCmd('at+clvl=8', .3)
        self.DUT.executeCmd('at+clvl=6', .3)

if __name__ == '__main__':
    unittest.main()