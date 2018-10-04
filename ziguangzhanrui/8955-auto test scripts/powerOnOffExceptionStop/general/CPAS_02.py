#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPAS_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPAS - 02 - Verify <pas>,  0 : ready  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPAS - 02 - Verify <pas>,  0 : ready  <<<<<<<<<<')

    def test_CPAS_02(self):
        self.DUT.executeCmd('at+cpas', .3, '+CPAS:0')

if __name__ == '__main__':
    unittest.main()