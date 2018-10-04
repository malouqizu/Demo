#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CACM_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CACM - 02 - Reset <acm> with <passwd>  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CACM - 02 - Reset <acm> with <passwd>  <<<<<<<<<<')

    def test_CACM_02(self):
        self.DUT.executeCmd('at+cacm="2345"', .3)

if __name__ == '__main__':
    unittest.main()