#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib import eueuser, euemongo, euehelpers


"""
Class dedicated to user authentication
"""


class auth:

    mongo = None
    collection = None
    user = None
    session = None

    def __init__(self, mongo, collection):
        self.mongo = mongo
        self.user = eueuser.user(self.mongo, self.collection)
        return

    def get_Session_Structure():
        return {
            "user": None,
            "password": None,
            "start": None,
            "end": None
        }

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
            usr = self.user.get(user=user)
            if not usr:
                return False
            else:
                if password != usr["password"]:
                    return False
                else:
                    self.session = self.get_Session_Structure()
                    self.session["user"] = user
                    self.session["password"] = password
                    return True

    def logout(self):
        """
        logout user
        """
        self.session = None
