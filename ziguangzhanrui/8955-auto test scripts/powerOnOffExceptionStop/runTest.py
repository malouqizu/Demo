#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import os
import datetime
from report.HTMLTestRunner import HTMLTestRunner

# modules
from general._general import GeneralSuite
from simstk._simstk import SimStkSuite
from phonebook._phonebook import PhonebookSuite
from audio._audio import AudioSuite
from call._call import CallSuite
from networkService._networkService import NetworkServiceSuite

# test suite
#MODULES = GeneralSuite
#MODULES = SimStkSuite
#MODULES = AudioTestSuite
#MODULES = CallSuite
#MODULES = NetworkServiceSuite
MODULES = GeneralSuite + SimStkSuite + PhonebookSuite + AudioSuite + CallSuite + NetworkServiceSuite

SUITE = unittest.TestSuite()
SUITE.addTests(MODULES)

# configure HTML report
dir = os.getcwd()
timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
output = open(dir + r'\result\rda8955_at_report-' + timeStamp + '.html', "wb")
runner = HTMLTestRunner(
    stream=output,
    title='RDA8955 AT Commands Test Report',
    description='Functional Test for RDA8955 AT Commands'
)

if __name__ == '__main__':
    # run the creted SUITE
    runner.run(SUITE)
