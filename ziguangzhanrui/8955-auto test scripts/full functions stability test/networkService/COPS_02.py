#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COPS_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COPS - 02 - Set <mode> to 0 : automatic  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< COPS - 02 - Set <mode> to 0 : automatic  <<<<<<<<<<')

    def test_COPS_02(self):
        self.DUT.executeCmd('at+cops=0', .3)

if __name__ == '__main__':
    unittest.main()