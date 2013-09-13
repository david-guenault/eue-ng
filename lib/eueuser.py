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

    def validate(self, user):
        """
        validate user dict format
        """

        """ validate user type (dict) """
        if not isinstance(user, dict):
            # print "Invalid type user"
            return False
        """ validate mandatory keys in dict """
        if not "email" in user or not "password" in user:
            # print "email and passord keys not present in user dict"
            return False

        """ validate mandatory values in dict """
        if user["email"] == "" or user["password"] == "":
            # print "email and password are required"
            return False

        """ validate email format """
        if not euehelpers.check_mail(user["email"]):
            # print "invalid email format"
            return False

        return True

    """ create a new user """
    def new(self, user):
        """ common validation """
        if not self.validate(user):
            return False

        """ first check if a document with the same email already exist """
        usr = self.get(user["email"])
        if usr:
            # print "user with the same email already exist"
            return False

        """ create new user """
        try:
            id = self.mongo.db[self.collection].insert(user)
            return id
        except:
            # print "Mongo client raise an insert exception"
            return False

    """ update user """
    def update(self, user):
        """ common validation """
        if not self.validate(user):
            return False
        else:
            criteria = {"email": user["email"]}
            del user["email"]

            try:
                self.mongo.db[self.collection].update(criteria, {"$set": user})
                return True
            except:
                # print "Mongo raise an update exception"
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
                # print "Mongo raise a remove exception"
                return False

    """ get a user """
    def get(self, user):
        # print "searching user %s" % user
        try:
            result = self.mongo.db[self.collection].find(
                {"email": user})
        except:
            # print "Mongo raise a find exception"
            return False

        if result.count() == 0:
            # print "No user found"
            return False

        if result.count() > 1:
            # print "More than one result when trying to get user"
            return False

        del result[0]["_id"]
        return result[0]

if __name__ == '__main__':
    from lib import euemongo
    m = euemongo.mongo(host="localhost", port=27017, database="eue")
    m.connect()
    u = user(m, "users")
    print u.new({"email": "david.guenault@gmail.com", "password": "dfgdfg"})
    print u.update({
        "email": "david.guenault@gmail.com",
        "password": "abcd",
        "firstname": "david"})
    print u.get("david.guenault@gmail.com")
    print u.delete("david.guenault@gmail.com")
    print m.disconnect()
