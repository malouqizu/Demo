#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from networkService.COPN_01 import COPN_01
from networkService.COPS_01 import COPS_01
from networkService.COPS_02 import COPS_02
from networkService.COPS_03 import COPS_03
from networkService.COPS_04 import COPS_04
from networkService.CREG_01 import CREG_01
from networkService.CREG_02 import CREG_02
from networkService.CREG_03 import CREG_03
from networkService.CREG_04 import CREG_04
from networkService.CSQ_01 import CSQ_01
from networkService.CSQ_02 import CSQ_02
from networkService.CPOL_01 import CPOL_01
from networkService.CCFC_01 import CCFC_01
from networkService.CCWA_01 import CCWA_01
from networkService.CLIP_01 import CLIP_01
from networkService.CLIR_01 import CLIR_01
from networkService.CLIR_02 import CLIR_02
from networkService.CLIR_03 import CLIR_03
from networkService.CLIR_04 import CLIR_04
from networkService.COLP_01 import COLP_01
from networkService.COLP_02 import COLP_02
from networkService.COLP_03 import COLP_03
from networkService.CSSN_01 import CSSN_01
from networkService.CSSN_02 import CSSN_02
from networkService.CSSN_03 import CSSN_03
from networkService.CUSD_01 import CUSD_01
from networkService.CUSD_02 import CUSD_02
from networkService.CUSD_03 import CUSD_03

# networkService cases
copn01 = unittest.TestLoader().loadTestsFromTestCase(COPN_01)
cops01 = unittest.TestLoader().loadTestsFromTestCase(COPS_01)
cops02 = unittest.TestLoader().loadTestsFromTestCase(COPS_02)
cops03 = unittest.TestLoader().loadTestsFromTestCase(COPS_03)
cops04 = unittest.TestLoader().loadTestsFromTestCase(COPS_04)
creg01 = unittest.TestLoader().loadTestsFromTestCase(CREG_01)
creg02 = unittest.TestLoader().loadTestsFromTestCase(CREG_02)
creg03 = unittest.TestLoader().loadTestsFromTestCase(CREG_03)
creg04 = unittest.TestLoader().loadTestsFromTestCase(CREG_04)
csq01 = unittest.TestLoader().loadTestsFromTestCase(CSQ_01)
csq02 = unittest.TestLoader().loadTestsFromTestCase(CSQ_02)
cpol01 = unittest.TestLoader().loadTestsFromTestCase(CPOL_01)
ccfc01 = unittest.TestLoader().loadTestsFromTestCase(CCFC_01)
ccwa01 = unittest.TestLoader().loadTestsFromTestCase(CCWA_01)
clip01 = unittest.TestLoader().loadTestsFromTestCase(CLIP_01)
clir01 = unittest.TestLoader().loadTestsFromTestCase(CLIR_01)
clir02 = unittest.TestLoader().loadTestsFromTestCase(CLIR_02)
clir03 = unittest.TestLoader().loadTestsFromTestCase(CLIR_03)
clir04 = unittest.TestLoader().loadTestsFromTestCase(CLIR_04)
colp01 = unittest.TestLoader().loadTestsFromTestCase(COLP_01)
colp02 = unittest.TestLoader().loadTestsFromTestCase(COLP_02)
colp03 = unittest.TestLoader().loadTestsFromTestCase(COLP_03)
cssn01 = unittest.TestLoader().loadTestsFromTestCase(CSSN_01)
cssn02 = unittest.TestLoader().loadTestsFromTestCase(CSSN_02)
cssn03 = unittest.TestLoader().loadTestsFromTestCase(CSSN_03)
cusd01 = unittest.TestLoader().loadTestsFromTestCase(CUSD_01)
cusd02 = unittest.TestLoader().loadTestsFromTestCase(CUSD_02)
cusd03 = unittest.TestLoader().loadTestsFromTestCase(CUSD_03)

# networkService test suite
NetworkServiceSuite = [
    copn01, cops01, cops02, cops03, cops04, creg01, creg02, creg03, creg04,
    csq01, csq02, cpol01, ccfc01, ccwa01, clip01, clir01, clir02, clir03,
    clir04, colp01, colp02, colp03, cssn01, cssn02, cssn03, cusd01, cusd02, cusd03 
]