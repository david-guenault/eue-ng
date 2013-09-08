#!/usr/bin/python
# -*- coding: <encoding name> -*-


class user:

    mongo = None
    collection = None

    def __init__(self, mongo=None, collection=None):
        self.mongo = mongo
        self.collection = collection
        return

    """ create a new user """
    def new(self, user=None, password=None):

        """ validate mandatory """
        if not user or not password:
            return False
        if user == "" or password == "":
            return False

        """ first check if a document with the same email already exist """
        user = self.get(user)
        if user:
            if user.count() > 0:
                return False

        """ create new user """
        id = self.mongo.db[self.collection].insert(
            {"email": user, "password": password})

        return id

    """ update user """
    def update(self, user, password):
        pass

    """ delete user """
    def delete(self, user, password):
        pass

    """ get a user """
    def get(self, user):
        try:
            result = self.mongo.db[self.collection].find(
                {"email": user})
            return result
        except:
            return False
