#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class X_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> X - 02 - set [<value>] to 1  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< X - 02 - set [<value>] to 1  <<<<<<<<<<')

    def test_X_02(self):
        self.DUT.executeCmd('atx1', .3)

if __name__ == '__main__':
    unittest.main()