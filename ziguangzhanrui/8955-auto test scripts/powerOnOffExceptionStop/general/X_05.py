#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class X_05(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> X - 05 - set [<value>] to 4  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< X - 05 - set [<value>] to 4  <<<<<<<<<<')

    def test_X_05(self):
        self.DUT.executeCmd('atx4', .3)

if __name__ == '__main__':
    unittest.main()