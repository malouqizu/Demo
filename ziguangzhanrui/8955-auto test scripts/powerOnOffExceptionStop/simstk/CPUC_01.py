#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPUC_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPUC- 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPUC- 01 - Test, read command  <<<<<<<<<<')

    def test_CPUC_01(self):
        self.DUT.executeCmd('at+cpuc=?', .3)
        self.DUT.executeCmd('at+cpuc?', .3)

if __name__ == '__main__':
    unittest.main()