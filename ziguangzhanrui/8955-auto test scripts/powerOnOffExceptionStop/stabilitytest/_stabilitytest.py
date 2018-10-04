#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from stabilitytest.BuildInConnect import BuildInConnect

# stabilitytest cases
BuildInConnectCase = unittest.TestLoader().loadTestsFromTestCase(BuildInConnect)

# stabilitytest test suite
BuildInConnectSuite = [
    BuildInConnectCase
]