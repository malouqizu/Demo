#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class VTD_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> VTD - 02 - Set <n> to 10, 5, 1 >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< VTD - 02 - Set <n> to 10, 5, 1  <<<<<<<<<<')

    def test_vtd_02(self):
        self.DUT.executeCmd('at+vtd=10', .3)
        self.DUT.executeCmd('at+vtd?', .3, '+VTD: 10')
        self.DUT.executeCmd('at+vtd=5', .3)
        self.DUT.executeCmd('at+vtd?', .3, '+VTD: 5')
        self.DUT.executeCmd('at+vtd=1', .3)
        self.DUT.executeCmd('at+vtd?', .3, '+VTD: 1')

if __name__ == '__main__':
    unittest.main()
    