#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class EGMR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> EGMR - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< EGMR - 01 - Test command  <<<<<<<<<<')

    def test_EGMR_01(self):
        self.DUT.executeCmd('at+egmr=?', .3, '+EGMR: (1,2),(7)')

if __name__ == '__main__':
    unittest.main()