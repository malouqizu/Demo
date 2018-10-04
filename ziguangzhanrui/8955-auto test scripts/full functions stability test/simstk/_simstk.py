#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from simstk.CPIN_01 import CPIN_01
from simstk.CPINC_01 import CPINC_01
from simstk.CPINC_02 import CPINC_02
from simstk.CPIN2_01 import CPIN2_01
from simstk.CPIN2_02 import CPIN2_02
from simstk.CLCK_01 import CLCK_01
from simstk.CLCK_02 import CLCK_02
from simstk.CLCK_05 import CLCK_05
from simstk.CPWD_01 import CPWD_01
from simstk.CRSM_01 import CRSM_01
from simstk.CRSM_02 import CRSM_02
from simstk.CRSM_03 import CRSM_03
from simstk.CNUM_01 import CNUM_01
from simstk.CNUM_02 import CNUM_02
from simstk.CACM_01 import CACM_01
from simstk.CACM_02 import CACM_02
from simstk.CAMM_01 import CAMM_01
from simstk.CAMM_02 import CAMM_02
from simstk.CPUC_01 import CPUC_01
from simstk.CPUC_02 import CPUC_02
from simstk.STA_01 import STA_01
from simstk.STGI_01 import STGI_01
from simstk.STR_01 import STR_01
from simstk.STF_01 import STF_01
from simstk.STF_02 import STF_02
from simstk.STF_03 import STF_03

# simstk cases
cpin01 = unittest.TestLoader().loadTestsFromTestCase(CPIN_01)
cpinc01 = unittest.TestLoader().loadTestsFromTestCase(CPINC_01)
cpinc02 = unittest.TestLoader().loadTestsFromTestCase(CPINC_02)
cpin201 = unittest.TestLoader().loadTestsFromTestCase(CPIN2_01)
cpin202 = unittest.TestLoader().loadTestsFromTestCase(CPIN2_02)
clck01 = unittest.TestLoader().loadTestsFromTestCase(CLCK_01)
clck02 = unittest.TestLoader().loadTestsFromTestCase(CLCK_02)
clck05 = unittest.TestLoader().loadTestsFromTestCase(CLCK_05)
cpwd01 = unittest.TestLoader().loadTestsFromTestCase(CPWD_01)
crsm01 = unittest.TestLoader().loadTestsFromTestCase(CRSM_01)
crsm02 = unittest.TestLoader().loadTestsFromTestCase(CRSM_02)
crsm03 = unittest.TestLoader().loadTestsFromTestCase(CRSM_03)
cnum01 = unittest.TestLoader().loadTestsFromTestCase(CNUM_01)
cnum02 = unittest.TestLoader().loadTestsFromTestCase(CNUM_02)
cacm01 = unittest.TestLoader().loadTestsFromTestCase(CACM_01)
cacm02 = unittest.TestLoader().loadTestsFromTestCase(CACM_02)
camm01 = unittest.TestLoader().loadTestsFromTestCase(CAMM_01)
camm02 = unittest.TestLoader().loadTestsFromTestCase(CAMM_02)
cpuc01 = unittest.TestLoader().loadTestsFromTestCase(CPUC_01)
cpuc02 = unittest.TestLoader().loadTestsFromTestCase(CPUC_02)
sta01 = unittest.TestLoader().loadTestsFromTestCase(STA_01)
stgi01 = unittest.TestLoader().loadTestsFromTestCase(STGI_01)
str01 = unittest.TestLoader().loadTestsFromTestCase(STR_01)
stf01 = unittest.TestLoader().loadTestsFromTestCase(STF_01)
stf02 = unittest.TestLoader().loadTestsFromTestCase(STF_02)
stf03 = unittest.TestLoader().loadTestsFromTestCase(STF_03)

# simstk test suite
SimStkSuite = [
    cpin01, cpinc01, cpinc02, cpin201, cpin202, clck01, clck02, clck05,
    cpwd01, crsm01, crsm02, crsm03, cnum01, cnum02, cacm01, cacm02, camm01,
    camm02, cpuc01, cpuc02, sta01, stgi01, str01, stf01, stf02, stf03
]