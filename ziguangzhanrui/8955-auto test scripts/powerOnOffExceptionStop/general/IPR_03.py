#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class IPR_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> IPR - 03 - Set <rate> to 115200  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< IPR - 03 - Set <rate> to 115200  <<<<<<<<<<')

    def test_IPR_03(self):
        self.DUT.executeCmd('at+ipr=115200', .3)
        self.DUT.executeCmd('at+ipr?', .3, '+IPR: 115200')

if __name__ == '__main__':
    unittest.main()