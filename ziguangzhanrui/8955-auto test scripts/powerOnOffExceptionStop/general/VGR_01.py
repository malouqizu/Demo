#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class VGR_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> VGR - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< VGR - 01 - Test, read command  <<<<<<<<<<')

    def test_VGR_01(self):
        self.DUT.executeCmd('at+vgr=?', .3, '+VGR: (5-8)')
        self.DUT.executeCmd('at+vgr?', .3, '+VGR: 6')

if __name__ == '__main__':
    unittest.main()