#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGACT_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGACT - 03 - Set <state> to 0 : deactivated  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGACT - 03 - Set <state> to 0 : deactivated  <<<<<<<<<<')

    def test_CGACT_03(self):
        self.DUT.executeCmd('at+cgact=0', 5)
        self.DUT.executeCmd('at+cgact?', 1)

if __name__ == '__main__':
    unittest.main()