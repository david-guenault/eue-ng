#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from lib import eueauth, euemongo, eueuser

"""
Unit tests for auth class module
"""


class TestAuth(unittest.TestCase):

    mongo = None
    host = "localhost"
    port = 27017
    database = "eue"
    collection = "users"

    def setUp(self):
        self.mongo = euemongo.mongo(
            host=self.host,
            port=self.port,
            database=self.database)
        self.mongo.connect()

    def tearDown(self):
        self.mongo.disconnect()
        self.mongo.db[self.collection].drop()

    def test001_login_logout(self):
        """ check login process """
        user = eueuser.user(self.mongo, "users")
        auth = eueauth.auth(self.mongo, "users")
        assert user.new("david.guenault@gmail.com", "dfgdfg")
        assert auth.logout()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
    unittest.TextTestRunner(verbosity=2).run(suite)
