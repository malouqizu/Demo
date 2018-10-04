#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class A_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> case title  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< case title  <<<<<<<<<<')

    def test_a_01(self):
        self.DUT.executeCmd('a', .3, 'xxx', 'yyy')

if __name__ == '__main__':
    unittest.main()