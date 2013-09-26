#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import simplejson
import os.path
import random
import sys
from lib import eueuser
from lib import euemongo

""" for user retrieval """

sex = ["male", "female"]
targetbase = "static/images/users"
urlbase = "http://api.randomuser.me/0.2/"

""" for mongo """

host = "localhost"
port = 27017
database = "eue"
collection = "users"


""" generate 25 male and 25 female """
generated = []
sequence = range(10)
for s in sex:
    for index in sequence:
        sys.stdout.write('.')
        sys.stdout.flush()
        response = urllib2.urlopen("%s/?results=5&gender=%s" % (urlbase, s))
        data = simplejson.load(response)
        for user in data["results"]:
            filename = user["user"]["picture"].split('/')[-1]
            """ grap picture localy """
            target = "%s/%s/%s" % (targetbase, s, filename)
            if not os.path.isfile(target):
                urllib.urlretrieve(user["user"]["picture"], target)

            isAdmin = random.sample([0, 1], 1)[0]

            u = {
                "firstname": user["user"]["name"]["first"],
                "lastname": user["user"]["name"]["last"],
                "email": user["user"]["email"],
                "password": user["user"]["password"],
                "picture": filename,
                "isAdmin": isAdmin
            }
            generated.append(u)

""" create users in database """

mongo = None
mongo = euemongo.mongo(
    host=host,
    port=port,
    database=database)
mongo.connect()
user = eueuser.user(mongo=mongo, collection=collection)

mongo.db.drop_collection(collection)

for u in generated:
    print user.new(u)
