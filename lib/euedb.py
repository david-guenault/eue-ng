#!/usr/bin/python
# -*- coding: <encoding name> -*-

import os
import sys
import time
import re
from pymongo import MongoClient


class mongo:

    from pymongo import MongoClient

    cn = None
    db = None

    host = None
    port = None
    user = None
    password = None
    database = None

    def __init__(
            self, host="localhost", port=27017,
            database=None, user=None, password=None):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        # try:
        self.cn = MongoClient(host=self.host, port=self.port)
        if self.database:
            self.db = self.cn[self.database]
        return True
        # except:
        #     return False

    def disconnect(self):
        try:
            self.cn.close()
            return True
        except:
            return False
