#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from lib import euedb

"""
Unit tests for euedb mongo class module
"""


class TestMongo(unittest.TestCase):

    c = None
    host = "localhost"
    db = "eue"
    port = 27017
    collection = "users"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test001_connect(self):
        """ test mongodb connection """
        self.c = euedb.mongo(host=self.host, port=self.port, db=self.db)
        assert c.connect()

    def test002_disconnect(self):
        """ test mongodb disconnection """
        assert self.c.disconnect()

if __name__ == '__main__':
    unittest.main()
