#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class ICF_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ICF - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ICF - 01 - Test, read command  <<<<<<<<<<')

    def test_ICF_01(self):
        self.DUT.executeCmd('at+icf=?', .3, '+ICF:(1-6),(0-3)')
        self.DUT.executeCmd('at+icf?', .3, '+ICF: 3, 0')

if __name__ == '__main__':
    unittest.main()