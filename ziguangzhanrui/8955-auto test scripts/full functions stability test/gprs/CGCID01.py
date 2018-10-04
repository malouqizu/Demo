#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGCID_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGCID - 01 - Test, execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGCID - 01 - Test, execute command  <<<<<<<<<<')

    def test_CGCID_01(self):
        self.DUT.executeCmd('at+cgcid=?', .3, '+CGCID: (1-7)')
        self.DUT.executeCmd('at+cgcid', .3, '+CGCID:1')

if __name__ == '__main__':
    unittest.main()