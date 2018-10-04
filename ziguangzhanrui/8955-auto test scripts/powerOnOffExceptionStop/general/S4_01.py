#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S4_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S4 - 01 - Read >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S4 - 01 - Read <<<<<<<<<<')

    def test_S4_01(self):
        self.DUT.executeCmd('ats4?', .3, ' 10')

if __name__ == '__main__':
    unittest.main()