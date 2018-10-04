#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CACM_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CACM - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CACM - 01 - Test, read command  <<<<<<<<<<')

    def test_CACM_01(self):
        self.DUT.executeCmd('at+cacm=?', .3)
        self.DUT.executeCmd('at+cacm?', 1, '+CACM: "000000"')

if __name__ == '__main__':
    unittest.main()