#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GMR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GMR - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GMR - 02 - Execute command  <<<<<<<<<<')

    def test_GMR_02(self):
        self.DUT.executeCmd('at+gmr', .3, '20120707')

if __name__ == '__main__':
    unittest.main()