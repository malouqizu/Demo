#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CUSD_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CUSD - 03 - Set <n> to 0 : disable the result code presentation to the TE  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CUSD - 03 - Set <n> to 0 : disable the result code presentation to the TE <<<<<<<<<<')

    def test_CUSD_03(self):
        self.DUT.executeCmd('at+cusd=0', .3)
        self.DUT.executeCmd('at+cusd?', .3, '+CUSD:0')

if __name__ == '__main__':
    unittest.main()
    