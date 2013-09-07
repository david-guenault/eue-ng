#!/usr/bin/python
# -*- coding: <encoding name> -*-

import os
import sys
import time
import re
# import _mysql
import MySQLdb
from MySQLdb import cursors


class mydb:

    cn = None

    host = None
    port = None
    user = None
    passw = None

    def __init__(self, host, user, passw, db, port=3306):
        self.port = port
        self.host = host
        self.user = user
        self.passw = passw
        self.db = db
        if not self.connect():
            return False

    def connect(self):
        """
        connect to the mysql db
        """
        try:
            self.cn = MySQLdb.connect(
                host=self.host, user=self.user, passwd=self.passw,
                db=self.db, port=self.port)
            return True
        except:
            return False

    def querySelect(self, query):
        """
        do the select query and return the result as an array of dictionaries
        """
        data = []
        cur = self.cn.cursor(cursors.DictCursor)
        try:
            cur.execute(query)
        except:
            return False

        data = cur.fetchall()
        cur.close()
        return data
