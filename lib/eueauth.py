#!/usr/bin/python
# -*- coding: <encoding name> -*-

import re
from lib import eueuser, euemongo


"""
Class dedicated to user authentication
"""


class auth:

    def __init__(self):
        self.user = eueuser.user(self.mongo, "users")
        return

    def check_fields(self, user, password):
        """
        check if fields are provided and are not empty
        """
        if len(user) == 0 or len(password) == 0:
            return False

        pass

    def login(self, user, password):
        """
        authenticate user agains mongo database
        """
        pass

    def logout(self):
        """
        logout user
        """
        pass
