#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class VTD_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> VTD - 01 - Test, read command >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< VTD - 01 - Test, read command  <<<<<<<<<<')

    def test_vtd_01(self):
        self.DUT.executeCmd('at+vtd=?', .3, '+VTD: (1-10)')
        self.DUT.executeCmd('at+vtd?', .3, '+VTD: 1')

if __name__ == '__main__':
    unittest.main()
    