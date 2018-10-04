#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from phonebook.CPBS_01 import CPBS_01
from phonebook.CPBS_02 import CPBS_02
from phonebook.CPBS_03 import CPBS_03
from phonebook.CPBS_04 import CPBS_04
from phonebook.CPBS_05 import CPBS_05
from phonebook.CPBR_01 import CPBR_01
from phonebook.CPBW_01 import CPBW_01
from phonebook.CPBF_01 import CPBF_01

# phonebook cases
cpbs01 = unittest.TestLoader().loadTestsFromTestCase(CPBS_01)
cpbs02 = unittest.TestLoader().loadTestsFromTestCase(CPBS_02)
cpbs03 = unittest.TestLoader().loadTestsFromTestCase(CPBS_03)
cpbs04 = unittest.TestLoader().loadTestsFromTestCase(CPBS_04)
cpbs05 = unittest.TestLoader().loadTestsFromTestCase(CPBS_05)
cpbr01 = unittest.TestLoader().loadTestsFromTestCase(CPBR_01)
cpbw01 = unittest.TestLoader().loadTestsFromTestCase(CPBW_01)
cpbf01 = unittest.TestLoader().loadTestsFromTestCase(CPBF_01)

# phonebook test suite
PhonebookSuite = [
    cpbs01, cpbs02, cpbs03, cpbs04, cpbs05, cpbr01, cpbw01, cpbf01
]
