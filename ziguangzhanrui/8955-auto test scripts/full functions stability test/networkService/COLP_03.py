#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class COLP_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> COLP - 03- Set <n> 1 : enable  >>>>>>>>>>')

    def tearDown(self):
        # print case title 'case title'
        print('<<<<<<<<<< COLP - 03- Set <n> 1 : enable <<<<<<<<<<')

    def test_COLP_03(self):
        self.DUT.executeCmd('at+colp=0', .3)

if __name__ == '__main__':
    unittest.main()
    