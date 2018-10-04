#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class X_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> X - 01 - set [<value>] to 0  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< X - 01 - set [<value>] to 0  <<<<<<<<<<')

    def test_X_01(self):
        self.DUT.executeCmd('atx0', .3)

if __name__ == '__main__':
    unittest.main()