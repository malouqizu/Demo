#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CNUM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CNUM - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CNUM - 02 - Execute command  <<<<<<<<<<')

    def test_CNUM02(self):
        self.DUT.executeCmd('at+cnum', .3)

if __name__ == '__main__':
    unittest.main()