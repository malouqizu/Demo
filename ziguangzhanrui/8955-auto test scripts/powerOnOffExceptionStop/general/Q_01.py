#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class Q_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> Q - 01 - set [<value>] to 0: DCE transmits result code  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< Q - 01 - set [<value>] to 0: DCE transmits result code  <<<<<<<<<<')

    def test_Q_01(self):
        self.DUT.executeCmd('atq0', .3)

if __name__ == '__main__':
    unittest.main()