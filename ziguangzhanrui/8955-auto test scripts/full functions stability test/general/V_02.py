#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT
import time

class V_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> V - 02 - Set [<value>] to 1  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< V - 02 - Set [<value>] to 1  <<<<<<<<<<')

    def test_V_02(self):
        self.DUT.executeCmd('atv1', .3)
        self.DUT.executeCmd('at', .3,)

if __name__ == '__main__':
    unittest.main()