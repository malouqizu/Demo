#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from call.D_01 import D_01
from call.DLST_01 import DLST_01
from call.CHUP_01 import CHUP_01
from call.CHLD_01 import CHLD_01
from call.CLCC_01 import CLCC_01
from call.CRC_01 import CRC_01
from call.VTD_01 import VTD_01
from call.VTD_02 import VTD_02
from call.VTS_01 import VTS_01

# call cases
d01 = unittest.TestLoader().loadTestsFromTestCase(D_01)
dlst01 = unittest.TestLoader().loadTestsFromTestCase(DLST_01)
chup01 = unittest.TestLoader().loadTestsFromTestCase(CHUP_01)
chld01 = unittest.TestLoader().loadTestsFromTestCase(CHLD_01)
clcc01 = unittest.TestLoader().loadTestsFromTestCase(CLCC_01)
crc01 = unittest.TestLoader().loadTestsFromTestCase(CRC_01)
vtd01 = unittest.TestLoader().loadTestsFromTestCase(VTD_01)
vtd02 = unittest.TestLoader().loadTestsFromTestCase(VTD_02)
vts01 = unittest.TestLoader().loadTestsFromTestCase(VTS_01)

# call test suite
CallSuite = [
    d01, dlst01, chup01, chld01, clcc01, crc01, vtd01, vtd02, vts01
]
