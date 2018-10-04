#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGDCONT_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGDCONT - 02 - Define a PDP content (cmcc : cmnet)  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGDCONT - 02 - Define a PDP content (cmcc : cmnet)  <<<<<<<<<<')

    def test_CGDCONT_02(self):
        self.DUT.executeCmd('at+cgdcont=1,"IP","CMNET"', .3)
        self.DUT.executeCmd('at+cgdcont?', .3, '+CGDCONT:1,"IP","CMNET",,0,0')

if __name__ == '__main__':
    unittest.main()