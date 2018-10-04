#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CEER_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CEER - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CEER - 01 - Test command  <<<<<<<<<<')

    def test_CEER_01(self):
        self.DUT.executeCmd('at+ceer=?', .3)

if __name__ == '__main__':
    unittest.main()