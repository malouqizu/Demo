#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from comm.atc import atLogger, atChat


class VTD(unittest.TestCase):
    """ test case """
    name = "VTD"

    @classmethod
    def setUpClass(cls):
        atChat.open()
        atLogger.case_start(cls.name)

    @classmethod
    def tearDownClass(cls):
        atLogger.case_end(cls.name)
        atChat.close()

    def test_01(self):
        self.assertTrue(atChat.send('at+vtd=?', 0.3))
        self.assertTrue(atChat.has('+VTD: (1-10)'))

    def test_02(self):
        for i in range(1, 11):
            with self.subTest(i=i):
                self.assertTrue(atChat.send('at+vtd=%d'%(i), 0.3))
                self.assertTrue(atChat.has_in_order(atChat.ECHO, atChat.OK))
                self.assertTrue(atChat.send('at+vtd?', 0.3))
                self.assertTrue(atChat.has_in_order(atChat.ECHO, '+VTD: %d'%(i), atChat.OK))

    def test_03(self):
        self.assertTrue(atChat.send('at+vtd=1', 0.3))
        self.assertTrue(atChat.has_in_order(atChat.ECHO, atChat.OK))
        for i in [-1, 0, 11, 20]:
            self.assertTrue(atChat.send('at+vtd=%d'%(i), 0.3))
            self.assertTrue(atChat.has_in_order(atChat.ECHO, atChat.ERROR))
        self.assertTrue(atChat.send('at+vtd?', 0.3))
        self.assertTrue(atChat.has_in_order(atChat.ECHO, '+VTD: 1', atChat.OK))
