#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBS_05(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBS - 05 - Set <storge> "LD" : SIM/UICC last dialling phonebook  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBS - 05 - Set <storge> "LD" : SIM/UICC last dialling phonebook  <<<<<<<<<<')

    def test_CPBS_05(self):
        self.DUT.executeCmd('at+cpbs="LD"', 3)
        self.DUT.executeCmd('at+cpbs?', 3)

if __name__ == '__main__':
    unittest.main()