#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CLIP_01(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CLIP - 01- Test,read command  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CLIP - 01- Test,read command <<<<<<<<<<')

    def test_CLIP_01(self):
        self.DUT.executeCmd('at+clip=?', .3, '+CLIP:(0,1)')

if __name__ == '__main__':
    unittest.main()
