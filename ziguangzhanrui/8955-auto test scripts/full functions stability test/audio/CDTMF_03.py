#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CDTMF_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CDTMF - 03 - Set  <DTMF> with <duration>  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<<  CDTMF - 03 - Set  <DTMF> with <duration>  <<<<<<<<<<')

    def test_cdtmf_03(self):
        self.DUT.executeCmd('at+cdtmf=1,5', .3)
        self.DUT.executeCmd('at+cdtmf=B,10', .3)
        self.DUT.executeCmd('at+cdtmf=*,8', .3)
        
if __name__ == '__main__':
    unittest.main()