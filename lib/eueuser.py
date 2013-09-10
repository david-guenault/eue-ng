#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib import euehelpers


class user:

    mongo = None
    collection = None

    def __init__(self, mongo, collection):
        self.mongo = mongo
        self.collection = collection
        return

    """ create a new user """
    def new(self, user, password):
        """ validate mandatory """
        if user == "" or password == "":
            return False

        """ validate email format """
        if not euehelpers.check_mail(user):
            return False

        """ first check if a document with the same email already exist """
        usr = self.get(user)
        if usr:
            if usr.count() > 0:
                return False

        """ create new user """
        id = self.mongo.db[self.collection].insert(
            {"email": user, "password": password})

        return id

    """ update user """
    def update(self, user, password):
        """ validate mandatory """
        if user == "" or password == "":
            return False

        """ validate email format """
        if not euehelpers.check_mail(user):
            return False
        else:
            try:
                self.mongo.db[self.collection].update(
                    {"email": user},
                    {"password": password})
                return True
            except:
                return False

    """ delete user """
    def delete(self, user):
        """ validate email format """
        if not euehelpers.check_mail(user):
            return False
        else:
            try:
                self.mongo.db[self.collection].remove({"email": user})
                return True
            except:
                return False

    """ get a user """
    def get(self, user):
        try:
            result = self.mongo.db[self.collection].find(
                {"email": user})
            return result
        except:
            return False

if __name__ == '__main__':
    from lib import euemongo
    m = euemongo.mongo(host="localhost", port=27017, database="eue")
    m.connect()
    u = user(m, "users")
    u.new("david.guenault@gmail.com", "dfgdfg")
    m.disconnect()
