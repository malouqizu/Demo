#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CCWA_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CCWA - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CCWA - 01 - Test, read command <<<<<<<<<<')

    def test_ccwa_01(self):
        self.DUT.executeCmd('at+ccwa=?', .3, '+CCWA:(0-1)')
        self.DUT.executeCmd('at+ccwa?', .3, '+CCWA: 0')
        
if __name__ == '__main__':
    unittest.main()