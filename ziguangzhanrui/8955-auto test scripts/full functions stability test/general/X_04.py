#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class X_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> X - 04 - set [<value>] to 3  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< X - 04 - set [<value>] to 3  <<<<<<<<<<')

    def test_X_04(self):
        self.DUT.executeCmd('atx3', .3)

if __name__ == '__main__':
    unittest.main()