#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CGREG_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CGREG - 02 - Set <n> to 1   >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CGREG - 02 - Set <n> to 1   <<<<<<<<<<')

    def test_CGREG_02(self):
        self.DUT.executeCmd('at+cgreg=1', .3)
        self.DUT.executeCmd('at+cgreg?', .3, '+CGREG: 1,1')

if __name__ == '__main__':
    unittest.main()