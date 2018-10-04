#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class STF_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^STF - 03 - Set <mode> to 1: TEXT mode  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^STF - 03 - Set <mode> to 1: TEXT mode  <<<<<<<<<<')

    def test_STF_03(self):
        self.DUT.executeCmd('at^stf=1', .3, 'Set STF: TEXT Mode')
        self.DUT.executeCmd('at^stf?', .3, '^STF: TEXT mode')

if __name__ == '__main__':
    unittest.main()