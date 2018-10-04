#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class STF_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^STF - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^STF - 01 - Test, read command  <<<<<<<<<<')

    def test_STF_01(self):
        self.DUT.executeCmd('at^stf=?', .3, '^STF: (0,1)')
        self.DUT.executeCmd('at^stf?', .3, '^STF: TEXT mode')

if __name__ == '__main__':
    unittest.main()