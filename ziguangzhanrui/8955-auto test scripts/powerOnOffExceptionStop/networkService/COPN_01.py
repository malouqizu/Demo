#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COPN_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COPN - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< COPN - 01 - Test command  <<<<<<<<<<')

    def test_COPN_01(self):
        self.DUT.executeCmd('at+copn=?', .3)

if __name__ == '__main__':
    unittest.main()