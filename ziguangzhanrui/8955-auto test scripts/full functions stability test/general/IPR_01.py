#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class IPR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> IPR - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< IPR - 01 - Test, read command  <<<<<<<<<<')

    def test_IPR_01(self):
        self.DUT.executeCmd('at+ipr=?', .3, '(2400,4800,9600,14400,19200,28800,33600,38400,57600,115200,230400,460800,921600,1843200)')
        self.DUT.executeCmd('at+ipr?', .3, '+IPR: 115200')

if __name__ == '__main__':
    unittest.main()