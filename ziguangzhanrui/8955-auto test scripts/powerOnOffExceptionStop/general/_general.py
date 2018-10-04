#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from general.CPOF_01 import CPOF_01
from general.S0_01 import S0_01
from general.S3_01 import S3_01
from general.S3_02 import S3_02
from general.S4_01 import S4_01
from general.S4_02 import S4_02
from general.S5_01 import S5_01
from general.S5_02 import S5_02
from general.F_01 import F_01
from general.V_02 import V_02
from general.E_01 import E_01
from general.E_02 import E_02
from general.W_01 import W_01
from general.Q_01 import Q_01
from general.X_01 import X_01
from general.X_02 import X_02
from general.X_03 import X_03
from general.X_04 import X_04
from general.X_05 import X_05
from general.Z_01 import Z_01
from general.CFUN_01 import CFUN_01
from general.CMEE_01 import CMEE_01
from general.CMEE_02 import CMEE_02
from general.CMEE_03 import CMEE_03
from general.CMEE_04 import CMEE_04
from general.CSCS_01 import CSCS_01
from general.CSCS_02 import CSCS_02
from general.CSCS_03 import CSCS_03
from general.CSCS_04 import CSCS_04
from general.CSCS_05 import CSCS_05
from general.CMUX_01 import CMUX_01
from general.ICF_01 import ICF_01
from general.ICF_02 import ICF_02
from general.IPR_01 import IPR_01
from general.IPR_02 import IPR_02
from general.IPR_03 import IPR_03
from general.GSN_01 import GSN_01
from general.GSN_02 import GSN_02
from general.GMM_01 import GMM_01
from general.GMM_02 import GMM_02
from general.CGMM_01 import CGMM_01
from general.CGMM_02 import CGMM_02
from general.GMR_01 import GMR_01
from general.GMR_02 import GMR_02
from general.CGMR_01 import CGMR_01
from general.CGMR_02 import CGMR_02
from general.GMI_01 import GMI_01
from general.GMI_02 import GMI_02
from general.CGMI_01 import CGMI_01
from general.CGMI_02 import CGMI_02
from general.I_01 import I_01
from general.CIMI_01 import CIMI_01
from general.CIMI_02 import CIMI_02
from general.EGMR_01 import EGMR_01
from general.EGMR_02 import EGMR_02
from general.EGMR_03 import EGMR_03
from general.CALA_01 import CALA_01
from general.CALA_02 import CALA_02
from general.VGR_01 import VGR_01
from general.VGR_02 import VGR_02
from general.CLVL_01 import CLVL_01
from general.CLVL_02 import CLVL_02
from general.CMUT_01 import CMUT_01
from general.CMUT_02 import CMUT_02
from general.CMUT_03 import CMUT_03
from general.CCLK_01 import CCLK_01
from general.CCLK_02 import CCLK_02
from general.CALD_01 import CALD_01
from general.CALD_02 import CALD_02
from general.CBC_01 import CBC_01
from general.CBCM_01 import CBCM_01
from general.CBCM_02 import CBCM_02
from general.CBCM_03 import CBCM_03
from general.CMER_01 import CMER_01
from general.CMER_02 import CMER_02
from general.CMER_03 import CMER_03
from general.CEER_01 import CEER_01
from general.CPAS_01 import CPAS_01
from general.CPAS_02 import CPAS_02

# general cases
cpof01 = unittest.TestLoader().loadTestsFromTestCase(CPOF_01)
s001 = unittest.TestLoader().loadTestsFromTestCase(S0_01)
s301 = unittest.TestLoader().loadTestsFromTestCase(S3_01)
s302 = unittest.TestLoader().loadTestsFromTestCase(S3_02)
s401 = unittest.TestLoader().loadTestsFromTestCase(S4_01)
s402 = unittest.TestLoader().loadTestsFromTestCase(S4_02)
s501 = unittest.TestLoader().loadTestsFromTestCase(S5_01)
s502 = unittest.TestLoader().loadTestsFromTestCase(S5_02)
f01 = unittest.TestLoader().loadTestsFromTestCase(F_01)
v02 = unittest.TestLoader().loadTestsFromTestCase(V_02)
e01 = unittest.TestLoader().loadTestsFromTestCase(E_01)
e02 = unittest.TestLoader().loadTestsFromTestCase(E_02)
w01 = unittest.TestLoader().loadTestsFromTestCase(W_01)
q01 = unittest.TestLoader().loadTestsFromTestCase(Q_01)
x01 = unittest.TestLoader().loadTestsFromTestCase(X_01)
x02 = unittest.TestLoader().loadTestsFromTestCase(X_02)
x03 = unittest.TestLoader().loadTestsFromTestCase(X_03)
x04 = unittest.TestLoader().loadTestsFromTestCase(X_04)
x05 = unittest.TestLoader().loadTestsFromTestCase(X_05)
z01 = unittest.TestLoader().loadTestsFromTestCase(Z_01)
cfun01 = unittest.TestLoader().loadTestsFromTestCase(CFUN_01)
cmee01 = unittest.TestLoader().loadTestsFromTestCase(CMEE_01)
cmee02 = unittest.TestLoader().loadTestsFromTestCase(CMEE_02)
cmee03 = unittest.TestLoader().loadTestsFromTestCase(CMEE_03)
cmee04 = unittest.TestLoader().loadTestsFromTestCase(CMEE_04)
cscs01 = unittest.TestLoader().loadTestsFromTestCase(CSCS_01)
cscs02 = unittest.TestLoader().loadTestsFromTestCase(CSCS_02)
cscs03 = unittest.TestLoader().loadTestsFromTestCase(CSCS_03)
cscs04 = unittest.TestLoader().loadTestsFromTestCase(CSCS_04)
cscs05 = unittest.TestLoader().loadTestsFromTestCase(CSCS_05)
cmux01 = unittest.TestLoader().loadTestsFromTestCase(CMUX_01)
icf01 = unittest.TestLoader().loadTestsFromTestCase(ICF_01)
icf02 = unittest.TestLoader().loadTestsFromTestCase(ICF_02)
ipr01 = unittest.TestLoader().loadTestsFromTestCase(IPR_01)
ipr02 = unittest.TestLoader().loadTestsFromTestCase(IPR_02)
ipr03 = unittest.TestLoader().loadTestsFromTestCase(IPR_03)
gsn01 = unittest.TestLoader().loadTestsFromTestCase(GSN_01)
gsn02 = unittest.TestLoader().loadTestsFromTestCase(GSN_02)
gmm01 = unittest.TestLoader().loadTestsFromTestCase(GMM_01)
gmm02 = unittest.TestLoader().loadTestsFromTestCase(GMM_02)
cgmm01 = unittest.TestLoader().loadTestsFromTestCase(CGMM_01)
cgmm02 = unittest.TestLoader().loadTestsFromTestCase(CGMM_02)
gmr01 = unittest.TestLoader().loadTestsFromTestCase(GMR_01)
gmr02 = unittest.TestLoader().loadTestsFromTestCase(GMR_02)
cgmr01 = unittest.TestLoader().loadTestsFromTestCase(CGMR_01)
cgmr02 = unittest.TestLoader().loadTestsFromTestCase(CGMR_02)
gmi01 = unittest.TestLoader().loadTestsFromTestCase(GMI_01)
gmi02 = unittest.TestLoader().loadTestsFromTestCase(GMI_02)
cgmi01 = unittest.TestLoader().loadTestsFromTestCase(CGMI_01)
cgmi02 = unittest.TestLoader().loadTestsFromTestCase(CGMI_02)
i01 = unittest.TestLoader().loadTestsFromTestCase(I_01)
cimi01 = unittest.TestLoader().loadTestsFromTestCase(CIMI_01)
cimi02 = unittest.TestLoader().loadTestsFromTestCase(CIMI_02)
egmr01 = unittest.TestLoader().loadTestsFromTestCase(EGMR_01)
egmr02 = unittest.TestLoader().loadTestsFromTestCase(EGMR_02)
egmr03 = unittest.TestLoader().loadTestsFromTestCase(EGMR_03)
cala01 = unittest.TestLoader().loadTestsFromTestCase(CALA_01)
cala02 = unittest.TestLoader().loadTestsFromTestCase(CALA_02)
vgr01 = unittest.TestLoader().loadTestsFromTestCase(VGR_01)
vgr02 = unittest.TestLoader().loadTestsFromTestCase(VGR_02)
clvl01 = unittest.TestLoader().loadTestsFromTestCase(CLVL_01)
clvl02 = unittest.TestLoader().loadTestsFromTestCase(CLVL_02)
cmut01 = unittest.TestLoader().loadTestsFromTestCase(CMUT_01)
cmut02 = unittest.TestLoader().loadTestsFromTestCase(CMUT_02)
cmut03 = unittest.TestLoader().loadTestsFromTestCase(CMUT_03)
cclk01 = unittest.TestLoader().loadTestsFromTestCase(CCLK_01)
cclk02 = unittest.TestLoader().loadTestsFromTestCase(CCLK_02)
cald01 = unittest.TestLoader().loadTestsFromTestCase(CALD_01)
cald02 = unittest.TestLoader().loadTestsFromTestCase(CALD_02)
cbc01 = unittest.TestLoader().loadTestsFromTestCase(CBC_01)
cbcm01 = unittest.TestLoader().loadTestsFromTestCase(CBCM_01)
cbcm02 = unittest.TestLoader().loadTestsFromTestCase(CBCM_02)
cbcm03 = unittest.TestLoader().loadTestsFromTestCase(CBCM_03)
cmer01 = unittest.TestLoader().loadTestsFromTestCase(CMER_01)
cmer02 = unittest.TestLoader().loadTestsFromTestCase(CMER_02)
cmer03 = unittest.TestLoader().loadTestsFromTestCase(CMER_03)
ceer01 = unittest.TestLoader().loadTestsFromTestCase(CEER_01)
cpas01 = unittest.TestLoader().loadTestsFromTestCase(CPAS_01)
cpas02 = unittest.TestLoader().loadTestsFromTestCase(CPAS_02)

# general test suite
GeneralSuite = [
    cpof01, s001, s301, s302, s401, s402, s501, s502, f01, v02, e01, e02, 
    w01, q01, x01, x02, x03, x04, x05, z01, cfun01, cmee01, cmee02, cmee03, 
    cmee04, cscs01, cscs02, cscs03, cscs04, cscs05, cmux01, icf01, icf02, 
    ipr01, ipr02, ipr03, gsn01, gsn02, gmm01, gmm02, cgmm01, cgmm02, gmr01, 
    gmr02, cgmr01, cgmr02, gmi01, gmi02, cgmi01, cgmi02, i01, cimi01, cimi02, 
    egmr01, egmr02, egmr03, cala01, cala02, vgr01, vgr02, clvl01, clvl02, cmut01,
    cmut02, cmut03, cclk01, cclk02, cald01, cald02, cbc01, cbcm01, cbcm02,
    cbcm03, cmer01, cmer02, cmer03, ceer01, cpas01, cpas02
]