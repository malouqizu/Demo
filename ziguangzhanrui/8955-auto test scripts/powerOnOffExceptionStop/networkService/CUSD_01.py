#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CUSD_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CUSD - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CUSD - 01 - Test, read command <<<<<<<<<<')

    def test_CUSD_01(self):
        self.DUT.executeCmd('at+cusd=?', .3, '+CUSD:(0-2)')
        self.DUT.executeCmd('at+cusd?', .3, '+CUSD:0')

if __name__ == '__main__':
    unittest.main()
    