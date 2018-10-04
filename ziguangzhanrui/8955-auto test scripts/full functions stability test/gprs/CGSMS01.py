#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGSMS_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGSMS - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGSMS - 01 - Test, read command  <<<<<<<<<<')

    def test_CGSMS_01(self):
        self.DUT.executeCmd('at+cgsms=?', .3, '+CGSMS:0,1,2,3')
        self.DUT.executeCmd('at+cgsms?', .3)

if __name__ == '__main__':
    unittest.main()