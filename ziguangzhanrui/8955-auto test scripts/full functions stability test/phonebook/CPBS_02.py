#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBS_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBS - 02 - Set <storge> "SM" : SIM/UICC phonebook  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBS - 02 - Set <storge> "SM" : SIM/UICC phonebook  <<<<<<<<<<')

    def test_CPBS_02(self):
        self.DUT.executeCmd('at+cpbs="SM"', 3)
        self.DUT.executeCmd('at+cpbs?', 3)

if __name__ == '__main__':
    unittest.main()