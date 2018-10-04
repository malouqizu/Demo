#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGPADDR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGPADDR - 02 - Show PDP address after activating PDP  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGPADDR - 02 - Show PDP address after activating PDP  <<<<<<<<<<')

    def test_CGPADDR_02(self):
        self.DUT.executeCmd('at+cgact=1', 5)
        self.DUT.executeCmd('at+cgpaddr=1', .3)

if __name__ == '__main__':
    unittest.main()