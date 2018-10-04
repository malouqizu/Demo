#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSSN_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSSN - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSSN - 01 - Test, read command <<<<<<<<<<')

    def test_cssn_01(self):
        self.DUT.executeCmd('at+cssn=?', .3, '+CSSN:(0-1),(0-1)')
        self.DUT.executeCmd('at+cssn?', .3, '+CSSN:0,0')
        
if __name__ == '__main__':
    unittest.main()