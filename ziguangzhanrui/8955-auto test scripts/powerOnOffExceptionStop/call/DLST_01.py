#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from comm.at import AtTest, COMPORT

class DLST_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> DLST - 01 -  Redial last  >>>>>>>>>>')
        self.DUT.executeCmd('atd10086;', .3)
        time.sleep(15)
        self.DUT.executeCmd('at+chup', 1)
        time.sleep(10)

    def tearDown(self):
        self.DUT.executeCmd('at+chup', 1)
        time.sleep(10)
        print('<<<<<<<<<< DLST - 01 -  Redial last  <<<<<<<<<<')

    def test_DLST_01(self):
        self.DUT.executeCmd('at+dlst', .3)
        time.sleep(15)

if __name__ == '__main__':
    unittest.main()
