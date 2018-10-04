#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class VTS_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> VTS - 01 - Test command >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< VTS - 01 - Test command  <<<<<<<<<<')

    def test_vts_01(self):
        self.DUT.executeCmd('at+vts=?', .3, '+VTS: (0-9,*,#,A,B,C,D),(1-10)')

if __name__ == '__main__':
    unittest.main()
    