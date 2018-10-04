#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class CPBS_04(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> CPBS - 04 - Set <storge> "FD" : SIM/USIM fixdialling phonebook  >>>>>>>>>>')

    def tearDown(self):
        print('<<<<<<<<<< CPBS - 04 - Set <storge> "FD" : SIM/USIM fixdialling phonebook  <<<<<<<<<<')

    def test_CPBS_04(self):
        self.DUT.executeCmd('at+cpbs="FD"', 3)
        self.DUT.executeCmd('at+cpbs?', 3)

if __name__ == '__main__':
    unittest.main()