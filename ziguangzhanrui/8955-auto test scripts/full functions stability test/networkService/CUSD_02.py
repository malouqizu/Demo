#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CUSD_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CUSD - 02 - Set <n> to 1 : enable the result code presentation to the TE  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CUSD - 02 - Set <n> to 1 : enable the result code presentation to the TE <<<<<<<<<<')

    def test_CUSD_02(self):
        self.DUT.executeCmd('at+cusd=1', .3)
        self.DUT.executeCmd('at+cusd?', .3, '+CUSD:1')

if __name__ == '__main__':
    unittest.main()