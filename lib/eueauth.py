#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib import eueuser, euemongo, euehelpers
import time

"""
Class dedicated to user authentication
"""


class auth:

    mongo = None
    collection = None
    user = None

    def __init__(self, mongo, collection):
        self.mongo = mongo
        self.collection = collection
        self.user = eueuser.user(self.mongo, self.collection)

    def check_fields(self, user, password):
        if len(user) == "" or len(password) == "":
            return False
        else:
            if not euehelpers.check_mail(user):
                return False
            else:
                return True

    def login(self, user, password):
        """
        authenticate user agains mongo database
        """
        if not self.check_fields(user, password):
            return False
        else:
            usr = self.user.get(user)
            if not usr:
                return False
            else:
                if password != usr["password"]:
                    return False
                else:
                    return True

if __name__ == '__main__':

    mongo = None
    host = "localhost"
    port = 27017
    database = "eue"
    collection = "users"

    mongo = euemongo.mongo(
        host=host,
        port=port,
        database=database)

    mongo.connect()

    user = eueuser.user(mongo, "users")
    auth = auth(mongo, "users")

    user.new("david.guenault@gmail.com", "dfgdfg")
    user.get("david.guenault@gmail.com")
    print auth.login("david.guenault@gmail.com", "dfgdfg")

    mongo.disconnect()
    mongo.db[collection].drop()
