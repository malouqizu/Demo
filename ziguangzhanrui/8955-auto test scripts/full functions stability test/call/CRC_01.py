#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CRC_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CRC - 01 - Test, read command >>>>>>>>>>')

    def tearDown(self):
        # print case title 'case title'
        print('<<<<<<<<<< CRC - 01 - Test, read command  <<<<<<<<<<')

    def test_crc_01(self):
        self.DUT.executeCmd('at+crc=?', .3, '+CRC: (0,1)')
        self.DUT.executeCmd('at+crc?', .3, '+CRC: 0')

if __name__ == '__main__':
    unittest.main()
    