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
            > try to create a user with blank user and password : should fail
            > try to create a user with a blank password : should fail
            > try to create a user with a blank email : should fail
            > try to create a user with user and password : should success
            > try to create a user with email allready in database should fail
        """
        user = {"email": "",
                "password": "",
                "firstname": "",
                "lastname": ""}
        assert not self.user.new(user)
        user = {"email": "david.guenault@gmail.com",
                "password": "",
                "firstname": "",
                "lastname": ""}
        assert not self.user.new(user)
        user = {"email": "",
                "password": "dfgdfg",
                "firstname": "",
                "lastname": ""}
        assert not self.user.new(user)
        user = {"email": "david.guenault@gmail.com",
                "password": "dfgdfg",
                "firstname": "",
                "lastname": ""}
        assert self.user.new(user) != ""
        user = {"email": "david.guenault@gmail.com",
                "password": "dfgdfg",
                "firstname": "",
                "lastname": ""}
        """ should not pass because user already exist """
        assert not self.user.new(user)

    """ test non admin user creation """
    def test002_createNonAdminUser(self):
        """ default should be a non admin user """
        user = self.user.getUserStructure()
        user["email"] = "david.guenault@gmail.com"
        user["password"] = "dfgdfg"
        user["firstname"] = "David"
        user["lastname"] = "GUENAULT"

        """ user must return non empty """
        result = self.user.new(user)
        assert result != ""

        """ get created user """
        u = self.user.get(user["email"])

        """ there should be an acl key and in acl """
        assert "acl" in u
        assert isinstance(u["acl"], dict)
        """ there should be an isAdmin key """
        assert "isAdmin" in u["acl"]
        """ user should not be admin by default """
        assert not u["acl"]["isAdmin"]

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

    """ test that dict passed to method are not altered """
    def test005_alteration(self):
        original = {"email": "david.guenault@gmail.com",
                    "password": "dfgdfg",
                    "firstname": "David",
                    "lastname": "GUENAULT",
                    "acl": {"isAdmin": True}}

        """ test for create """
        clone = original.copy()
        self.user.new(clone)
        """ check we have the same number of elements for _id """
        assert len(original) == len(clone)
        """ check keys are not altered """
        for key in original:
            assert key in clone
            assert original[key] == clone[key]
        """ test for update """
        clone = original.copy()
        self.user.update(clone)
        """ check we have the same number of elements """
        assert len(original) == len(clone)
        """ check keys are not altered """
        for key in original:
            assert key in clone
            assert original[key] == clone[key]
        """ no test for delete because string is immutable """

    def test006_search(self):
        """ test user search """
        """ create a set of users """
        users = [{"email": "david.guenault@gmail.com",
                  "password": "dfgdfg",
                  "firstname": "David",
                  "lastname": "GUENAULT"},
                 {"email": "naparuba@gmail.com",
                  "password": "dfgdfg",
                  "firstname": "Jean",
                  "lastname": "GABES"},
                 {"email": "toto@titi.com",
                  "password": "dfgdfg",
                  "firstname": "toto",
                  "lastname": "TITI"}]
        for user in users:
            self.user.new(user)

        """ pattern to serch """
        pattern = "gmail.com"

        """ search coverage """
        where = ["email", "firstname", "lastname", "email"]

        """ do the search in regex mode """
        result = self.user.findregex(pattern, where)

        """ test result count should be 2 records """
        assert result is not False
        assert not isinstance(result, bool)
        assert len(result) == 2
        """ if no result should return empty list """
        # pattern = "42"
        # result = self.user.findregex(pattern, where)
        # print result
        # assert result is not False

if __name__ == '__main__':
    unittest.main()
