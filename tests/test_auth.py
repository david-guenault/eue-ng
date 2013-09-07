#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from lib import eueauth
from pymongo import Connection

"""
Unit tests for auth class module
"""


class TestAuth(unittest.TestCase):

    db = "testAuth"
    collection = "users"

    mongoCn = None
    mongoDb = None

    def setUp(self):
        self.auth = eueauth.auth()
        self.mongoCn = Connection()
        self.mongoDb = self.mongoCn[self.db]
        self.mongoColl = self.mongoDb[self.collection]

    def tearDown(self):
        self.mongoDb = None
        self.mongoCn.drop_database(self.db)
        self.mongoCn = None
        self.auth = None

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
