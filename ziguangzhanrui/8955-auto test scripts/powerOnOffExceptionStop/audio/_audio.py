#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

# import cases
from audio.CAUDIO_01 import CAUDIO_01
from audio.CAUDIO_02 import CAUDIO_02
from audio.CAUDIO_03 import CAUDIO_03
from audio.CRSL_01 import CRSL_01
from audio.CRSL_02 import CRSL_02
from audio.CRSL_03 import CRSL_03
from audio.CDTMF_01 import CDTMF_01
from audio.CDTMF_02 import CDTMF_02
from audio.CDTMF_03 import CDTMF_03
from audio.AUST_01 import AUST_01
from audio.AUST_02 import AUST_02
from audio.AUST_03 import AUST_03
from audio.AUST_04 import AUST_04

caudio01 = unittest.TestLoader().loadTestsFromTestCase(CAUDIO_01)
caudio02 = unittest.TestLoader().loadTestsFromTestCase(CAUDIO_02)
caudio03 = unittest.TestLoader().loadTestsFromTestCase(CAUDIO_03)
crsl01 = unittest.TestLoader().loadTestsFromTestCase(CRSL_01)
crsl02 = unittest.TestLoader().loadTestsFromTestCase(CRSL_02)
crsl03 = unittest.TestLoader().loadTestsFromTestCase(CRSL_03)
cdtmf01 = unittest.TestLoader().loadTestsFromTestCase(CDTMF_01)
cdtmf02 = unittest.TestLoader().loadTestsFromTestCase(CDTMF_02)
cdtmf03 = unittest.TestLoader().loadTestsFromTestCase(CDTMF_03)
aust01 = unittest.TestLoader().loadTestsFromTestCase(AUST_01)
aust02 = unittest.TestLoader().loadTestsFromTestCase(AUST_02)
aust03 = unittest.TestLoader().loadTestsFromTestCase(AUST_03)
aust04 = unittest.TestLoader().loadTestsFromTestCase(AUST_04)

# audio test suite
AudioSuite = [
    caudio01, caudio02, caudio03, crsl01, crsl02, crsl03,
    cdtmf01, cdtmf02, cdtmf03, aust01, aust02, aust03, aust04
]