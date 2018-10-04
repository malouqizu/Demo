#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.at import AtTest, COMPORT

class E_02(unittest.TestCase):
    
    def setUp(self):
        self.DUT = AtTest(COMPORT)
        print('\n>>>>>>>>>> E - 02 - Set <value> to 0 : Echo mode off  >>>>>>>>>>')

    def tearDown(self):
        self.DUT.executeCmd('ate1', .3)
        print('<<<<<<<<<< E - 02 - Set <value> to 0 : Echo mode off  <<<<<<<<<<')

    def test_E_02(self):
        self.DUT.executeCmd('ate0', .3)
        self.DUT.executeCmd('at', .3)        

if __name__ == '__main__':
    unittest.main()