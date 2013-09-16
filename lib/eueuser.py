#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib import euehelpers


class user:

    mongo = None
    collection = None
    userlog = []

    def __init__(self, mongo, collection):
        self.mongo = mongo
        self.collection = collection
        return

    def log(self,
            scope="private", source="",
            mtype="danger", content="", data=""):
        self.userlog.append({
            "order": len(self.userlog)+1,
            "scope": scope,
            "source": source,
            "type": mtype,
            "content": content,
            "data": data})

    def validate(self, user):
        """
        validate user dict format
        """

        """ validate user type (dict) """
        if not isinstance(user, dict):
            self.log(source="validate", content="Invalid user type", data=user)
            return False
        """ validate mandatory keys in dict """
        if not "email" in user or not "password" in user:
            content = "email and passord keys not present in user dict"
            self.log(source="validate",
                     content=content,
                     data=user)
            return False
        """ validate mandatory values in dict """
        if user["email"] == "" or user["password"] == "":
            self.log(source="validate",
                     content="email and password are required", data=user)
            return False
        """ validate email format """
        if not euehelpers.check_mail(user["email"]):
            self.log(source="validate",
                     content="invalid email format",
                     data=user)
            return False
        self.log(mtype="success",
                 source="validate",
                 content="Validation ok",
                 data=user)
        return True

    def validateUpdate(self, user):
        """
        validate user dict format only for update
        """

        """ validate user type (dict) """
        if not isinstance(user, dict):
            self.log(source="validateUpdate",
                     content="Invalid user type",
                     data=user)
            return False
        """ validate mandatory keys in dict """
        if not "email" in user:
            self.log(source="validateUpdate",
                     content="email key not present in user dict",
                     data=user)
            return False
        """ if password in dict it should not be empty """
        if "password" in user:
            if len(user["password"]) == 0:
                self.log(source="validateUpdate",
                         content="password should not be empty",
                         data=user)
                return False
        """ validate mandatory values in dict """
        if user["email"] == "":
            self.log(source="validateUpdate",
                     content="email should not be empty",
                     data=user)
            return False
        """ validate email format """
        if not euehelpers.check_mail(user["email"]):
            self.log(source="validateUpdate",
                     content="invalid email format",
                     data=user)
            return False
        """ validation ok """
        self.log(mtype="success",
                 source="validateUpdate",
                 content="Validation ok",
                 data=user)
        return True

    """ create a new user """
    def new(self, user):
        """ common validation """
        if not self.validate(user):
            return False

        clone = user.copy()

        """ first check if a document with the same email already exist """
        usr = self.get(clone["email"])
        if usr:
            self.log(source="new",
                     content="user with the same email already exist",
                     data=clone)
            return False

        """ create new user """
        try:
            id = self.mongo.db[self.collection].insert(clone)
            self.log(mtype="success",
                     source="new",
                     content="added user with id %s" % id,
                     data=clone)
            return id
        except:
            self.log(source="new",
                     content="Mongo client raise an insert exception",
                     data=clone)
            return False

    """ update user """
    def update(self, user):
        """ common validation """
        if not self.validateUpdate(user):
            return False
        else:
            email = user["email"]
            criteria = {"email": user["email"]}
            del user["email"]
            try:
                self.mongo.db[self.collection].update(criteria, {"$set": user})
                user["email"] = email
                return True
            except:
                self.log(source="update",
                         content="Mongo client raise an update exception",
                         data=user)
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
                self.log(source="update",
                         content="Mongo raise a remove exception",
                         data=user)
                return False

    """ get a user """
    def get(self, user):
        try:
            result = self.mongo.db[self.collection].find(
                {"email": user})
        except:
            self.log(source="get",
                     content="Mongo raise a find exception",
                     data=user)
            return False

        if result.count() == 0:
            self.log(source="get", content="No user found", data=user)
            return False

        if result.count() > 1:
            self.log(source="get",
                     content="More than one result when trying to get user",
                     data=user)
            return False

        del result[0]["_id"]
        return result[0]

if __name__ == '__main__':
    from lib import euemongo
    m = euemongo.mongo(host="localhost", port=27017, database="eue")
    m.connect()
    u = user(m, "users")
    u.log(source="instance", content="delete user", data={})
    u.delete("david.guenault@gmail.com")
    u.log(source="instance", content="new user", data={})
    u.new({"email": "david.guenault@gmail.com", "password": "dfgdfg"})
    u.log(source="instance", content="update user", data={})
    u.update({
        "email": "david.guenaultgmail.com",
        "firstname": "david",
        "lastname": "guenault",
        "password": ""})
    u.log(source="instance", content="get user", data={})
    u.get("david.guenault@gmail.com")
    u.log(source="instance", content="delete user", data={})
    u.delete("david.guenault@gmail.com")
    m.disconnect()
    print "+{:-^114}+".format("")
    topHeader = "| {:>5} | {:<15} | {:<10} | {:<10} | {:<60} |"
    rowContent = "| {:>5} | {:<15} | {:<10} | {:<10} | {:<60} |"
    print topHeader.format("order", "source", "scope", "type", "content")
    print "+{:-^114}+".format("")
    for line in u.userlog:
        print rowContent.format(line["order"],
                                line["source"],
                                line["scope"],
                                line["type"],
                                line["content"])
    print "+{:-^114}+".format("")
