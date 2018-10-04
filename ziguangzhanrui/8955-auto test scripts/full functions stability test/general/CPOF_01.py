#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPOF_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPOF - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPOF - 01 - Test, read command  <<<<<<<<<<')

    def test_a_01(self):
        self.DUT.executeCmd('at+cpof=?', .3)

if __name__ == '__main__':
    unittest.main()