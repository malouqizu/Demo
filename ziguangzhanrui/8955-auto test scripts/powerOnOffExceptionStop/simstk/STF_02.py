#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class STF_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> ^STF - 02 - Set <mode> to 0: PDU mode  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< ^STF - 02 - Set <mode> to 0: PDU mode  <<<<<<<<<<')

    def test_STF_02(self):
        self.DUT.executeCmd('at^stf=0', .3, 'Set STF: PDU Mode')
        self.DUT.executeCmd('at^stf?', .3, '^STF: PDU mode')

if __name__ == '__main__':
    unittest.main()