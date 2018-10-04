#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COLP_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COLP - 02 - Set <n> 0 : disable  >>>>>>>>>>')

    def tearDown(self):
        # print case title 'case title'
        print('<<<<<<<<<< COLP - 02 - Set <n> 0 : disable <<<<<<<<<<')

    def test_COLP_02(self):
        self.DUT.executeCmd('at+colp=0', .3)

if __name__ == '__main__':
    unittest.main()
    