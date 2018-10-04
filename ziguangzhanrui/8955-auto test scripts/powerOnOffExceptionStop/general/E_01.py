#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class E_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> E - 01 - Set <value> to 1 : Echo mode on  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< E - 01 - Set <value> to 1 : Echo mode on  <<<<<<<<<<')

    def test_E_01(self):
        self.DUT.executeCmd('ate1', .3)
        self.DUT.executeCmd('at', .3)

if __name__ == '__main__':
    unittest.main()