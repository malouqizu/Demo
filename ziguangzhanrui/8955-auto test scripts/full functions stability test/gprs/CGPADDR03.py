#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGPADDR_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGPADDR - 03 - Show PDP address after deactivating PDP  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGPADDR - 03 - Show PDP address after deactivating PDP  <<<<<<<<<<')

    def test_CGPADDR_03(self):
        self.DUT.executeCmd('at+cgact=0', 5)
        self.DUT.executeCmd('at+cgpaddr=1', .3)

if __name__ == '__main__':
    unittest.main()