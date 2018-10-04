#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CIMI_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CIMI - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CIMI - 02 - Execute command  <<<<<<<<<<')

    def test_CIMI_02(self):
        self.DUT.executeCmd('at+cimi', .3)

if __name__ == '__main__':
    unittest.main()