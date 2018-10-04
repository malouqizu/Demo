#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPIN2_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPIN2 - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPIN2 - 01 - Test, read command  <<<<<<<<<<')

    def test_CPIN2_01(self):
        self.DUT.executeCmd('at+cpin2=?', .3)
        self.DUT.executeCmd('at+cpin2?', .3, '+CPIN2: READY')

if __name__ == '__main__':
    unittest.main()