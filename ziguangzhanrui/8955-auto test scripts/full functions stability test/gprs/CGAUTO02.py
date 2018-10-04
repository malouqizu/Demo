#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGAUTO_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGAUTO - 02 - Set <n> to 1  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGAUTO - 02 - Set <n> to 1  <<<<<<<<<<')

    def test_CGAUTO_02(self):
        self.DUT.executeCmd('at+cgauto=1', .3)
        self.DUT.executeCmd('at+cgauto?', .3)

if __name__ == '__main__':
    unittest.main()