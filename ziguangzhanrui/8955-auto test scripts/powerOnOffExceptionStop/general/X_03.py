#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class X_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> X - 03 - set [<value>] to 2  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< X - 03 - set [<value>] to 2  <<<<<<<<<<')

    def test_X_03(self):
        self.DUT.executeCmd('atx2', .3)

if __name__ == '__main__':
    unittest.main()