#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPWD_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPWD - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPWD - 01 - Test command  <<<<<<<<<<')

    def test_CPWD_01(self):
        self.DUT.executeCmd('at+cpwd=?', .3, '+CPWD: ("SC",8),("P2",8)')

if __name__ == '__main__':
    unittest.main()