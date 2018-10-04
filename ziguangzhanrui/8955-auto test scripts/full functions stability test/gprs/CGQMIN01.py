#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGQMIN_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGQMIN - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGQMIN - 01 - Test, read command  <<<<<<<<<<')

    def test_CGQMIN_01(self):
        self.DUT.executeCmd('at+cgqmin=?', 1, 
        '+CGQMIN: IP, (0..3), (0..4), (0..5) , (0..9), (0..18,31)', 
        '+CGQMIN: PPP, (0..3), (0..4), (0..5) , (0..9), (0..18,31)', 
        '+CGQMIN: IPV6, (0..3), (0..4), (0..5) , (0..9), (0..18,31)')
        self.DUT.executeCmd('at+cgqmin?', 1,
        '+CGQMIN:1,0,0,0,0,0',
        '+CGQMIN:2,0,0,0,0,0',
        '+CGQMIN:3,0,0,0,0,0',
        '+CGQMIN:4,0,0,0,0,0',
        '+CGQMIN:5,0,0,0,0,0',
        '+CGQMIN:6,0,0,0,0,0',
        '+CGQMIN:7,0,0,0,0,0')

if __name__ == '__main__':
    unittest.main()