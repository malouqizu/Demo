#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGMI_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGMI - 02 - Execute command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGMI - 02 - Execute command  <<<<<<<<<<')

    def test_GMI_02(self):
        self.DUT.executeCmd('at+cgmi', .3, 'RDA')

if __name__ == '__main__':
    unittest.main()