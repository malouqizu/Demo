#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRSL_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRSL - 03- Set <value> to the default 6  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+crsl=6', .3)
        print('<<<<<<<<<<  CRSL - 03- Set <value> to the default 6 <<<<<<<<<<')

    def test_crsl_03(self):
        self.DUT.executeCmd('at+crsl=6', .3)
        self.DUT.executeCmd('at+crsl?', .3, '+CRSL: 6')

if __name__ == '__main__':
    unittest.main()