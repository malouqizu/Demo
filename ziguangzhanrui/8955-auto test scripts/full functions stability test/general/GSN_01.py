#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GSN_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GSN - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< GSN - 01 - Test command  <<<<<<<<<<')

    def test_GSN_01(self):
        self.DUT.executeCmd('at+gsn=?', .3)

if __name__ == '__main__':
    unittest.main()