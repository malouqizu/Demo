#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class Z_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> Z - 01 - Set all current parameters to user defined profilea  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< Z - 01 - Set all current parameters to user defined profile  <<<<<<<<<<')

    def test_Z_01(self):
        self.DUT.executeCmd('ats0?', .3, '0')
        self.DUT.executeCmd('ats0=5', .3)
        self.DUT.executeCmd('ats0?', .3, '5')
        self.DUT.executeCmd('atz', .3)
        self.DUT.executeCmd('ats0?', .3, '0')

if __name__ == '__main__':
    unittest.main()