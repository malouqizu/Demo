#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CALA_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CALA - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CALA - 01 - Test, read command  <<<<<<<<<<')

    def test_CALA_01(self):
        self.DUT.executeCmd('at+cala=?', .3, '+CALA: (1-15),(0),(32),(15)')

if __name__ == '__main__':
    unittest.main()