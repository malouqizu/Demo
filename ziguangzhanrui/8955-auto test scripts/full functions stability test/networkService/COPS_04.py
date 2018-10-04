#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COPS_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COPS - 04 - Set <mode> to 1 : manual, <format> to 2  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< COPS - 04 - Set <mode> to 1 : manual, <format> to 2  <<<<<<<<<<')

    def test_COPS_04(self):
        self.DUT.executeCmd('at+cops=1,2,"46000"', .3)
        self.DUT.executeCmd('AT+COPS?', .3)

if __name__ == '__main__':
    unittest.main()
