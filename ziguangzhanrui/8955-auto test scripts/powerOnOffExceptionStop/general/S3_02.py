#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S3_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S3 - 02 - Set <n> to 13 (default) >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S3 - 02 - Set <n> to 13 (default) <<<<<<<<<<')

    def test_S3_02(self):
        self.DUT.executeCmd('ats3=13', .3)
        self.DUT.executeCmd('ats3?', .3, ' 13')

if __name__ == '__main__':
    unittest.main()