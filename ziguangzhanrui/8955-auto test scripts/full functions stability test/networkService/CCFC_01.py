#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CCFC_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CCFC - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CCFC - 01 - Test command <<<<<<<<<<')

    def test_CCFC_01(self):
        self.DUT.executeCmd('at+ccfc=?', .3, '+CCFC:(0-5)')

if __name__ == '__main__':
    unittest.main()
