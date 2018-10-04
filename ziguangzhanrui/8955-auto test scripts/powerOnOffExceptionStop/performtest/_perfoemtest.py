#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from performtest.RegisterNetTime import RegisterNet
from performtest.AttachActiveTime import AttachActive
from performtest.CSQvalue import CSQvalue
from performtest.PoweronATReady import PowerOnTime
from performtest.TCPIP import Tcpip

# performtest cases
RegstNetCase = unittest.TestLoader().loadTestsFromTestCase(RegisterNet)
AttachActiveCase = unittest.TestLoader().loadTestsFromTestCase(AttachActive)
CSQValueCase = unittest.TestLoader().loadTestsFromTestCase(CSQvalue)
PowerOnTimeCase = unittest.TestLoader().loadTestsFromTestCase(PowerOnTime)
TcpIpCase = unittest.TestLoader().loadTestsFromTestCase(Tcpip)

# performtest test suite
PerformSuite = [
    RegstNetCase, AttachActiveCase, CSQValueCase, PowerOnTimeCase, TcpIpCase
]
