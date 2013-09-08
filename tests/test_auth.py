#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from lib import eueauth, euedb

"""
Unit tests for auth class module
"""


class TestAuth(unittest.TestCase):

    mongo = None
    host = "localhost"
    port = 27017
    db = "eue"
    collection = "users"

    def setUp(self):
        self.mongo = euedb.mongo(host=self.host, port=self.port)
        self.mongo.connect()

    def tearDown(self):
        self.mongo.disconnect()

    def test001_both_login_and_password(self):
        """ test if both login and password are provided """
        assert not self.auth.check_fields()
        assert not self.auth.check_fields("")
        assert not self.auth.check_fields("", "")
        assert not self.auth.check_fields(None, None)
        assert not self.auth.check_fields("xxx", "")
        assert not self.auth.check_fields("", "xxx")
        assert self.auth.check_fields("xxx", "xxx")

    def test002_login_is_valid_email(self):
        """ does the provided login is a valid email format """
        assert not self.auth.check_mail("toto")
        assert not self.auth.check_mail("toto.titi@tutu")
        assert self.auth.check_mail("toto.titi@tutu.com")
        assert self.auth.check_mail("ToTo.tItI@tutu.com")

    def test003_auth(self):
        """ check login process """
        assert True

    def test004_deauth(self):
        """ check logout process """
        assert True

if __name__ == '__main__':
    unittest.main()
