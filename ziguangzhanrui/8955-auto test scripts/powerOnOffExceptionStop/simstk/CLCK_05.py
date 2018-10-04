#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLCK_05(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLCK - 05 - Set <fac> to "FD", <mode> to 2 : query status  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLCK - 05 - Set <fac> to "FD", <mode> to 2 : query status  <<<<<<<<<<')

    def test_CLCK_05(self):
        self.DUT.executeCmd('at+clck="FD",2', .3, '+CLCK:0')

if __name__ == '__main__':
    unittest.main()