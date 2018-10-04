#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CDTMF_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CDTMF - 01 - Test command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  CDTMF - 01 - Test command <<<<<<<<<<')

    def test_cdtmf_01(self):
        self.DUT.executeCmd('at+cdtmf=?', .3, '^CDTMF: (0-9,*,#,A,B,C,D),(1-10)')

if __name__ == '__main__':
    unittest.main()