#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from lib import eueuser
from pymongo import Connection

"""
Unit tests for user class module
"""


class TestUser(unittest.TestCase):

    db = "eue"
    collection = "users"

    mongoCn = None
    mongoDb = None

    def setUp(self):
        self.user = eueuser.user()
        self.mongoCn = Connection()
        self.mongoDb = self.mongoCn[self.db]
        self.mongoColl = self.mongoDb[self.collection]

    def tearDown(self):
        self.mongoDb = None
        self.mongoCn.drop_database(self.db)
        self.mongoCn = None
        self.auth = None

    """ test user creation """
    def test001_createUser(self):
        """
            try to create a user with blank user and password : should fail
            try to create a user with a blank password : should fail
            try to create a user with a blank email : should fail
            try to create a user with user and password : should success
            try to create a user with email allready in database should fail
        """
        cases = [
            {"email": "",
                "password": "",
                "assert": False},
            {"email": "david.guenault@gmail.com",
                "password": "",
                "assert": False},
            {"email": "",
                "password": "dfgdfg",
                "assert": False},
            {"email": "david.guenault@gmail.com",
                "password": "dfgdfg",
                "assert": True},
            {"email": "david.guenault@gmail.com",
                "password": "dfgdfg",
                "assert": False}]

        for case in cases:
            if not case["assert"]:
                assert not self.user.new(case["email"], case["password"])
            else:
                assert self.user.new(case["email"], case["password"])

    """ test user update """
    def test001_updateUser(self):
        """
            create a user
            update the password
            try to update with an empty password
        """
        assert self.user.new("david.guenault@gmail.com", "abcd")
        assert self.user.update("david.guenault@gmail.com", "efgh")
        assert not self.user.update("david.guenault@gmail.com", "")

    """ test user deletion """
    def test001_updateUser(self):
        """
            create a user
            delete the user for an exisiting user
            delete the user for an unknown user
            delete the user with an empty email
        """
        assert self.user.new("david.guenault@gmail.com", "abcd")
        assert self.user.delete("david.guenault@gmail.com")
        assert not self.user.delete("david@gmail.com")
        assert not self.user.delete("")

if __name__ == '__main__':
    unittest.main()
