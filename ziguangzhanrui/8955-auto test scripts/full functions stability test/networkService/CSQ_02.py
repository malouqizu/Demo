#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CSQ_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CSQ - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CSQ - 02 - Execute command  <<<<<<<<<<')

    def test_CSQ_02(self):
        self.DUT.executeCmd('at+csq', .3)

if __name__ == '__main__':
    unittest.main()
