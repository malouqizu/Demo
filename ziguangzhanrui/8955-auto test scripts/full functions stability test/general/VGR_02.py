#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class VGR_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> VGR - 02 - Set <n> to 5, 7, 8, 6  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< VGR - 02 - Set <n> to 5, 7, 8, 6  <<<<<<<<<<')

    def test_VGR_02(self):
        self.DUT.executeCmd('at+vgr=5', .3)
        self.DUT.executeCmd('at+vgr=7', .3)
        self.DUT.executeCmd('at+vgr=8', .3)
        self.DUT.executeCmd('at+vgr=6', .3)

if __name__ == '__main__':
    unittest.main()