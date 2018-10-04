#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class S3_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> S3 - 01 - Read >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< S3 - 01 - Read <<<<<<<<<<')

    def test_S3_01(self):
        self.DUT.executeCmd('ats3?', .3, ' 13')

if __name__ == '__main__':
    unittest.main()