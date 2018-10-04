#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGSMS_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGSMS - 03 - Set <service> to 2   >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGSMS - 03 - Set <service> to 2   <<<<<<<<<<')

    def test_CGSMS_02(self):
        self.DUT.executeCmd('at+cgsms=2', .3)
        self.DUT.executeCmd('at+cgsms?', .3, '+CGSMS:2')

if __name__ == '__main__':
    unittest.main()