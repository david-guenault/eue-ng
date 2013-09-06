#!/usr/bin/env python
import os
import sys
from bottle import route,run,template,static_file
#from lib import mydb

base=os.path.dirname(os.path.realpath(__file__))

dom0s = []
capacity = []

def getDataStructure():
    return {
        "title" : "",
        "page" : "login.tpl",
        "nav" : True
    }

@route('/static/<filename:path>')
def static(filename):
    """ return static files """
    return static_file(filename,root="%s/static" % (base))

@route('/')
def index():
    """ index page """
    data = getDataStructure()
    return template('index',page='index',data=data)

@route('/login')
def login():
    """ authentication page """
    data = getDataStructure()
    data["nav"] = False
    return template('login',page='login',data=data)


run(host='localhost',port=8080,reloader=True,debug=True)