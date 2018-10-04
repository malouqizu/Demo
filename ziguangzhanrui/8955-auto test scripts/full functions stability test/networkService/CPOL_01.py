#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPOL_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPOL - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPOL - 01 - Test, read command  <<<<<<<<<<')

    def test_cpol_01(self):
        self.DUT.executeCmd('at+cpol=?', .3)
        self.DUT.executeCmd('at+cpol?', .3)

if __name__ == '__main__':
    unittest.main()