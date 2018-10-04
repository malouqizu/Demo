#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CHUP_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CHUP - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CHUP - 01 - Test command  <<<<<<<<<<')

    def test_chup_01(self):
        self.DUT.executeCmd('at+chup=?', .3)

if __name__ == '__main__':
    unittest.main()
    