#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CALA_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CALA - 02 - Set alarm <time>  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CALA - 02 - Set alarm <time>  <<<<<<<<<<')

    def test_CALA_02(self):
        self.DUT.executeCmd('at+cala="17/12/20,15:05:00",1,0,"a1"', .3)
        self.DUT.executeCmd('at+cala?', .3, '+CALA: "17/12/20,15:05:00",1,0,"a1"')

if __name__ == '__main__':
    unittest.main()