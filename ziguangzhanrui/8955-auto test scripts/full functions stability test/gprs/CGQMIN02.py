#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGQMIN_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGQMIN - 02 - Set all parameters to 1  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGQMIN - 02 - Set all parameters to 1  <<<<<<<<<<')

    def test_CGQMIN_02(self):
        self.DUT.executeCmd('at+cgqmin=1,1,1,1,1,1', 1, '+CGQMIN:1,1,1,1,1,1')
        self.DUT.executeCmd('at+cgqmin?', 1,
        '+CGQMIN:1,1,1,1,1,1',
        '+CGQMIN:2,0,0,0,0,0',
        '+CGQMIN:3,0,0,0,0,0',
        '+CGQMIN:4,0,0,0,0,0',
        '+CGQMIN:5,0,0,0,0,0',
        '+CGQMIN:6,0,0,0,0,0',
        '+CGQMIN:7,0,0,0,0,0')

if __name__ == '__main__':
    unittest.main()