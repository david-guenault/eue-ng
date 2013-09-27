#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import re
from pymongo import MongoClient
from bson.json_util import dumps

host = "localhost"
port = 27017
database = "eue"
collection = "users"

cn = MongoClient(host=host, port=port)
print cn
db = cn[database]
print db
co = db[collection]
print co
regex = re.compile(".*", re.IGNORECASE)

result = co.find()

"""
    [{"$match": {"$or": [{"email": ".*"},
                         {"firstname": ".*"}]}},
"""

result = co.aggregate([{'$match': {'$or': [{'email': regex}, 
										   {'firstname': regex}, 
										   {'lastname': regex}, 
										   {'email': regex}]}}, 
						{'$project': {'firstname': '$firstname', 
									  'lastname': '$lastname', 
									  'isAdmin': '$isAdmin', 
									  '_id': 0, 
									  'email': '$email', 
									  'select': {'$toLower':''}}}])

print dumps(result)

cn.close()
