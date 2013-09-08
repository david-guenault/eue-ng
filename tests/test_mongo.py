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
        """ test mongodb connection/disconnection """
        self.c = euedb.mongo(host=self.host, port=self.port, database=self.db)
        assert self.c.connect() is True
        assert self.c.disconnect()

if __name__ == '__main__':
    unittest.main()
