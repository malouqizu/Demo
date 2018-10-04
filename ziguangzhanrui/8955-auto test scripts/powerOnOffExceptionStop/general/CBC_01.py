#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CBC_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CBC - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CBC - 01 - Test, read command  <<<<<<<<<<')

    def test_CBC_01(self):
        self.DUT.executeCmd('at+cbc=?', .3, '+CBC: (0-5),(0,10,20,30,40,50,60,70,80,90,100)')
        self.DUT.executeCmd('at+cbc?', .3)

if __name__ == '__main__':
    unittest.main()