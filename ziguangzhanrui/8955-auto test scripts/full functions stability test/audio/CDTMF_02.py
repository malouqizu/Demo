#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CDTMF_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CDTMF - 02 - Set  <DTMF> without <duration>  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  CDTMF - 02 - Set  <DTMF> without <duration>  <<<<<<<<<<')

    def test_cdtmf_02(self):
        self.DUT.executeCmd('at+cdtmf=8', .3)
        self.DUT.executeCmd('at+cdtmf=#', .3)
        self.DUT.executeCmd('at+cdtmf=D', .3)
        
if __name__ == '__main__':
    unittest.main()