#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S5_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S5 - 01 - Read >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S5 - 01 - Read <<<<<<<<<<')

    def test_S5_01(self):
        self.DUT.executeCmd('ats5?', .3, '  8')

if __name__ == '__main__':
    unittest.main()