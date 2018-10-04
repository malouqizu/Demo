#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COPS_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COPS - 03 - Set <mode> to 1 : manual, <format> to 0 >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< COPS - 03 - Set <mode> to 1 : manual, <format> to 0 <<<<<<<<<<')

    def test_COPS_03(self):
        self.DUT.executeCmd('at+cops=1,0,"ChinaMobile"', 3)
        self.DUT.executeCmd('at+cops?', .3)

if __name__ == '__main__':
    unittest.main()
    