#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGACT_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGACT - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGACT - 01 - Test, read command  <<<<<<<<<<')

    def test_CGACT_01(self):
        self.DUT.executeCmd('at+cgact=?', .3, '+CGACT: (0,1)')
        self.DUT.executeCmd('at+cgact?', 1)

if __name__ == '__main__':
    unittest.main()