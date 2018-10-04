#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRSL_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRSL - 02 - Set <value> to 0, 5,15  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('at+crsl=6', .3)
        print('<<<<<<<<<<  CRSL - 02 - Set <value> to 0, 5,15  <<<<<<<<<<')

    def test_crsl_02(self):
        self.DUT.executeCmd('at+crsl=0', .3)
        self.DUT.executeCmd('at+crsl?', .3, '+CRSL: 0')
        self.DUT.executeCmd('at+crsl=5', .3)
        self.DUT.executeCmd('at+crsl?', .3, '+CRSL: 5')
        self.DUT.executeCmd('at+crsl=15', .3)
        self.DUT.executeCmd('at+crsl?', .3, '+CRSL: 15')

if __name__ == '__main__':
    unittest.main()