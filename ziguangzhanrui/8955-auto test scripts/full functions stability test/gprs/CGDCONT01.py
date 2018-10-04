#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGDCONT_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGDCONT - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGDCONT - 01 - Test, read command  <<<<<<<<<<')

    def test_CGDCONT_01(self):
        self.DUT.executeCmd('at+cgdcont=?', .3, '+CGDCONT: (1..7), (IP,IPV6,PPP),(0..3),(0..4)')
        self.DUT.executeCmd('at+cgdcont?', .3)

if __name__ == '__main__':
    unittest.main()