#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from gprs.CGACT01 import CGACT_01
from gprs.CGACT02 import CGACT_02
from gprs.CGACT03 import CGACT_03
from gprs.CGATT01 import CGATT_01
from gprs.CGATT02 import CGATT_02
from gprs.CGATT03 import CGATT_03
from gprs.CGAUTO01 import CGAUTO_01
from gprs.CGAUTO02 import CGAUTO_02
from gprs.CGCID01 import CGCID_01
from gprs.CGDCONT01 import CGDCONT_01
from gprs.CGDCONT02 import CGDCONT_02
from gprs.CGPADDR01 import CGPADDR_01
from gprs.CGPADDR01 import CGPADDR_01
from gprs.CGPADDR02 import CGPADDR_02
from gprs.CGPADDR03 import CGPADDR_03
from gprs.CGQMIN01 import CGQMIN_01
from gprs.CGQMIN02 import CGQMIN_02
from gprs.CGREG01 import CGREG_01
from gprs.CGREG02 import CGREG_02
from gprs.CGREG03 import CGREG_03
from gprs.CGSMS01 import CGSMS_01
from gprs.CGSMS02 import CGSMS_02

# gprs cases
cgact01 = unittest.TestLoader().loadTestsFromTestCase(CGACT_01)
cgact02 = unittest.TestLoader().loadTestsFromTestCase(CGACT_02)
cgact03 = unittest.TestLoader().loadTestsFromTestCase(CGACT_03)
cgatt01 = unittest.TestLoader().loadTestsFromTestCase(CGATT_01)
cgatt02 = unittest.TestLoader().loadTestsFromTestCase(CGATT_02)
cgatt03 = unittest.TestLoader().loadTestsFromTestCase(CGATT_03)
cgauto01 = unittest.TestLoader().loadTestsFromTestCase(CGAUTO_01)
cgauto02 = unittest.TestLoader().loadTestsFromTestCase(CGAUTO_02)
cgcid01 = unittest.TestLoader().loadTestsFromTestCase(CGCID_01)
cgdcont01 = unittest.TestLoader().loadTestsFromTestCase(CGDCONT_01)
cgdcont02 = unittest.TestLoader().loadTestsFromTestCase(CGDCONT_02)
cgpaddr01 = unittest.TestLoader().loadTestsFromTestCase(CGPADDR_01)
cgpaddr02 = unittest.TestLoader().loadTestsFromTestCase(CGPADDR_02)
cgpaddr03 = unittest.TestLoader().loadTestsFromTestCase(CGPADDR_03)
cgqmin01 = unittest.TestLoader().loadTestsFromTestCase(CGQMIN_01)
cgqmin02 = unittest.TestLoader().loadTestsFromTestCase(CGQMIN_02)
cgreg01 = unittest.TestLoader().loadTestsFromTestCase(CGREG_01)
cgreg02 = unittest.TestLoader().loadTestsFromTestCase(CGREG_02)
cgreg03 = unittest.TestLoader().loadTestsFromTestCase(CGREG_03)
cgsms01 = unittest.TestLoader().loadTestsFromTestCase(CGSMS_01)
cgsms02 = unittest.TestLoader().loadTestsFromTestCase(CGSMS_02)

# gprs test suite
GprsSuite = [
    cgact01, cgact02, cgact03, cgatt01, cgatt02, cgatt03, cgauto01, cgauto02,
    cgcid01, cgdcont01, cgdcont02, cgpaddr01, cgpaddr02, cgpaddr03, cgqmin01,
    cgqmin02, cgreg01, cgreg02, cgreg03, cgsms01, cgsms02
    ]

