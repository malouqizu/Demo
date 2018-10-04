#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CNUM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CNUM - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CNUM - 01 - Test command  <<<<<<<<<<')

    def test_CNUM01(self):
        self.DUT.executeCmd('at+cnum=?', .3)

if __name__ == '__main__':
    unittest.main()