#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGMI_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGMI - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGMI - 01 - Test command  <<<<<<<<<<')

    def test_CGMI_01(self):
        self.DUT.executeCmd('at+cgmi=?', .3)

if __name__ == '__main__':
    unittest.main()