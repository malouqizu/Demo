#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLCK_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLCK - 02 - Set <fac> to "SC", <mode> to 2 : query status  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLCK - 02 - Set <fac> to "SC", <mode> to 2 : query status  <<<<<<<<<<')

    def test_CLCK_02(self):
        self.DUT.executeCmd('at+clck="SC",2', .3, '+CLCK:0')

if __name__ == '__main__':
    unittest.main()