#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class ICF_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ICF - 02 - Set <format> to 3, <parity> to 3  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ICF - 02 - Set <format> to 3, <parity> to 3  <<<<<<<<<<')

    def test_ICF_02(self):
        self.DUT.executeCmd('at+icf=3,3', .3)
        self.DUT.executeCmd('at+icf?', .3, '+ICF: 3, 3')

if __name__ == '__main__':
    unittest.main()