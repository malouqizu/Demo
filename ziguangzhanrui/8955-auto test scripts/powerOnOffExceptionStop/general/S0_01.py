#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S0_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S0 - 01 - Test, read command >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S0 - 01 - Test, read command <<<<<<<<<<')

    def test_S0_01(self):
        self.DUT.executeCmd('ats0=?', .3, '0-255')
        self.DUT.executeCmd('ats0?', .3, '0')

if __name__ == '__main__':
    unittest.main()