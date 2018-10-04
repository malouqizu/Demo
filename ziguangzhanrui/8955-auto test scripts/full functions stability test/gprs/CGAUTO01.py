#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGAUTO_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGAUTO - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGAUTO - 01 - Test, read command  <<<<<<<<<<')

    def test_CGAUTO_01(self):
        self.DUT.executeCmd('at+cgauto=?', .3, '+CGAUTO: (0-3)')
        self.DUT.executeCmd('at+cgauto?', .3)

if __name__ == '__main__':
    unittest.main()