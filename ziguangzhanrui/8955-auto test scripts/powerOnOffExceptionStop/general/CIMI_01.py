#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CIMI_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CIMI - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CIMI - 01 - Test command  <<<<<<<<<<')

    def test_CIMI_01(self):
        self.DUT.executeCmd('at+cimi=?', .3)

if __name__ == '__main__':
    unittest.main()