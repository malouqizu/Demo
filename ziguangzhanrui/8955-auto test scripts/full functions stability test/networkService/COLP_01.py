#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COLP_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COLP - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< COLP - 01 - Test command <<<<<<<<<<')

    def test_COLP_01(self):
        self.DUT.executeCmd('at+colp=?', .3, '+COLP:(0,1)')

if __name__ == '__main__':
    unittest.main()
