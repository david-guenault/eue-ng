#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from lib import euemongo
from lib import eueuser

"""
Unit tests for user class module
"""


class TestUser(unittest.TestCase):

    host = "localhost"
    port = 27017
    database = "eue"
    collection = "users"

    mongo = None

    def setUp(self):
        self.mongo = euemongo.mongo(
            host=self.host,
            port=self.port,
            database=self.database)
        self.mongo.connect()
        self.user = eueuser.user(mongo=self.mongo, collection=self.collection)

    def tearDown(self):
        """ unset user instance """
        self.user = None
        """ cleanup everything for next test """
        self.mongo.db.drop_collection(self.collection)
        """ disconnect from mongo """
        self.mongo.disconnect()
        """ unset mongo instance """
        self.mongo = None

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
                "firstname": "",
                "lastname": "",
                "assert": False},
            {"email": "david.guenault@gmail.com",
                "password": "",
                "firstname": "",
                "lastname": "",
                "assert": False},
            {"email": "",
                "password": "dfgdfg",
                "firstname": "",
                "lastname": "",
                "assert": False},
            {"email": "david.guenault@gmail.com",
                "password": "dfgdfg",
                "firstname": "",
                "lastname": "",
                "assert": "notempty"},
            {"email": "david.guenault@gmail.com",
                "password": "dfgdfg",
                "firstname": "",
                "lastname": "",
                "assert": False}]

        for case in cases:
            if not case["assert"]:
                assert not self.user.new(case)
            if case["assert"]:
                assert self.user.new(case)
            if case["assert"] is "notempty":
                assert self.user.new(case) != ""

    """ test get user """
    def test002_getUser(self):
        id = self.user.new({
            "email": "david.guenault@gmail.com",
            "password": "abcd"})
        assert id is not False
        result = self.user.get("david.guenault@gmail.com")
        assert result is not False
        assert result['_id'] == id
        assert result['email'] == 'david.guenault@gmail.com'
        assert result['password'] == 'abcd'

    """ test user update """
    def test003_updateUser(self):
        """ create a user """
        assert self.user.new({
            "email": "david.guenault@gmail.com",
            "password": "dfgdfg",
            "firstname": "Eric",
            "lastname": "SORIANO"})
        """ update the password / firstname / lastname """
        assert self.user.update({
            "email": "david.guenault@gmail.com",
            "password": "abcd",
            "firstname": "David",
            "lastname": "GUENAULT"})
        """ verify that everything is really updated """
        usr = self.user.get("david.guenault@gmail.com")
        assert usr["email"] == "david.guenault@gmail.com"
        assert usr["password"] == "abcd"
        assert usr["firstname"] == "David"
        assert usr["lastname"] == "GUENAULT"
        """ try to update with an empty email """
        assert not self.user.update({
            "email": "",
            "password": "dfgdfg",
            "firstname": "David",
            "lastname": "GUENAULT"})
        """ try to update with an empty password """
        assert not self.user.update({
            "email": "david.guenault@gmail.com",
            "password": "",
            "firstname": "David",
            "lastname": "GUENAULT"})
        """ try to update with an empty password and an empty email """
        assert not self.user.update({
            "email": "",
            "password": "",
            "firstname": "David",
            "lastname": "GUENAULT"})
        """ try to update only firstname and lastname """
        assert self.user.update({
            "email": "david.guenault@gmail.com",
            "firstname": "David",
            "lastname": "GUENAULT"})

        print self.user.get("david.guenault@gmail.com")

    """ test user deletion """
    def test004_deleteUser(self):
        """
            create a user
            delete the user for an exisiting user
            delete the user for an unknown user
            delete the user with an empty email
        """
        assert self.user.new({
            "email": "david.guenault@gmail.com",
            "password": "abcd"})
        assert self.user.delete("david.guenault@gmail.com")

if __name__ == '__main__':
    unittest.main()
