#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGREG_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGREG - 01 - Test, read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGREG - 01 - Test, read command  <<<<<<<<<<')

    def test_CGREG_01(self):
        self.DUT.executeCmd('at+cgreg=?', .3)
        self.DUT.executeCmd('at+cgreg?', .3)

if __name__ == '__main__':
    unittest.main()