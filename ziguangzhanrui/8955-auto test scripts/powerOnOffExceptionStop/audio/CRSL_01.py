#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRSL_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRSL - 01 - Test, read command   >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CRSL - 01 - Test, read command   <<<<<<<<<<')

    def test_crsl_01(self):
        self.DUT.executeCmd('at+crsl=?', .3, '+CRSL: (0-15)')
        self.DUT.executeCmd('at+crsl?', .3, '+CRSL: 6')

if __name__ == '__main__':
    unittest.main()