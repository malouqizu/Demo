#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGACT_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGACT - 02 - Set <state> to 1 : activated  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGACT - 02 - Set <state> to 1 : activated  <<<<<<<<<<')

    def test_CGACT_02(self):
        self.DUT.executeCmd('at+cgact=1', 5)
        self.DUT.executeCmd('at+cgact?', 1)

if __name__ == '__main__':
    unittest.main()