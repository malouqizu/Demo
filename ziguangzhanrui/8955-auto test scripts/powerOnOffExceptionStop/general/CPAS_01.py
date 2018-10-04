#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPAS_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPAS - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPAS - 01 - Test command  <<<<<<<<<<')

    def test_CPAS_01(self):
        self.DUT.executeCmd('at+cpas=?', .3, '+CPAS:0,1,3,4')

if __name__ == '__main__':
    unittest.main()