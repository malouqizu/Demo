#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class I_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> I - 01 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< I - 01 - Execute command  <<<<<<<<<<')

    def test_I_01(self):
        self.DUT.executeCmd('ati', .3, 'RDA', 'RDA MODULE ID', '20120707')

if __name__ == '__main__':
    unittest.main()