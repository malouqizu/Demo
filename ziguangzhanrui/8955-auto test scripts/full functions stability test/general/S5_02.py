#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S5_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S5 - 02 - Set <n> to 8 (default) >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S5 - 02 - Set <n> to 8 (default) <<<<<<<<<<')

    def test_S5_02(self):
        self.DUT.executeCmd('ats5=8', .3)
        self.DUT.executeCmd('ats5?', .3, '  8')

if __name__ == '__main__':
    unittest.main()