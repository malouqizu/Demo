#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class GSN_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> GSN - 02 - Execute command  >>>>>>>>>>')
        self.DUT.executeCmd('at+egmr=1,7,"012345678901234"', .3)

    def tearDown(self):
        print('<<<<<<<<<< GSN - 02 - Execute command  <<<<<<<<<<')

    def test_GSN_02(self):
            self.DUT.executeCmd('at+gsn', .3, '012345678901234')

if __name__ == '__main__':
        unittest.main()