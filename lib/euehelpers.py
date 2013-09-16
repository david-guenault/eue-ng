#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

"""
helpers functions for various aspect of eue-ng project
"""


def check_mail(email):
    """
    Verify that the provided email is valid
    """

    regex = r"^[_.0-9A-Za-z-]+@([0-9A-Za-z][0-9A-Za-z-]+.)+[A-Za-z]{2,4}$"
    try:
        if not re.match(regex, email):
            return False
        else:
            return True
    except:
        return False
