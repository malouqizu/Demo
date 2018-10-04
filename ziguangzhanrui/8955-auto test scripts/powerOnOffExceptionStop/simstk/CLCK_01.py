#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLCK_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLCK - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLCK - 01 - Test command  <<<<<<<<<<')

    def test_CLCK_01(self):
        self.DUT.executeCmd('at+clck=?', .3, '+CLCK: ("SC","FD","AO","OX","OI")')

if __name__ == '__main__':
    unittest.main()