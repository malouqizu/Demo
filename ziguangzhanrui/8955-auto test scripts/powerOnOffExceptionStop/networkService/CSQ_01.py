#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSQ_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSQ - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSQ - 01 - Test command  <<<<<<<<<<')

    def test_CSQ_01(self):
        self.DUT.executeCmd('at+csq=?', .3, '+CSQ: (0-31,99),(0-7,99)')

if __name__ == '__main__':
    unittest.main()
