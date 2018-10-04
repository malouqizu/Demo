#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S4_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S4 - 02 - Set <n> to 10 (default) >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S4 - 02 - Set <n> to 10 (default) <<<<<<<<<<')

    def test_S4_02(self):
        self.DUT.executeCmd('ats4=10', .3)
        self.DUT.executeCmd('ats4?', .3, ' 10')

if __name__ == '__main__':
    unittest.main()