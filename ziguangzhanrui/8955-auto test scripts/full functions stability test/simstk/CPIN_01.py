#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPIN_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPIN - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPIN - 01 - Test, read command  <<<<<<<<<<')

    def test_CPIN_01(self):
        self.DUT.executeCmd('at+cpin=?', .3)
        self.DUT.executeCmd('at+cpin?', .3, '+CPIN:READY')

if __name__ == '__main__':
    unittest.main()