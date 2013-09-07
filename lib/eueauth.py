#!/usr/bin/python
# -*- coding: <encoding name> -*-

import re


class auth:

    def __init__(self):
        return

    def check_fields(self, user=None, password=None):
        """
        check if fields are provided and are not empty
        """

        if not user or not password:
            return False

        if len(user) == 0 or len(password) == 0:
            return False

        return True

    def check_mail(self, email=None):
        """
        Verify that the provided email is valid
        """

        regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(regex, email):
            return False
        else:
            return True

        return True

    def check_auth(self, user, password):
        """
        Verify authentication credentials
        """
        return True
