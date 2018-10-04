#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class IPR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> IPR - 02 - Set <rate> to 57600  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+ipr=115200', .3)
        print('<<<<<<<<<< IPR - 02 - Set <rate> to 57600  <<<<<<<<<<')

    def test_IPR_02(self):
        self.DUT.executeCmd('at+ipr=57600', .3)
        self.DUT.executeCmd('at+ipr?', .3, '+IPR: 57600')

if __name__ == '__main__':
    unittest.main()