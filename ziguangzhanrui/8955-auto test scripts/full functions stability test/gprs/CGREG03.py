#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGREG_03(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGREG - 03 - Set <n> to 2   >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGREG - 03 - Set <n> to 2   <<<<<<<<<<')

    def test_CGREG_03(self):
        self.DUT.executeCmd('at+cgreg=2', .3)
        self.DUT.executeCmd('at+cgreg?', .3)

if __name__ == '__main__':
    unittest.main()