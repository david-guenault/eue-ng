#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from bottle import route, run, template, static_file, get, post
from lib import eueauth


def getDataStructure():
    """ initialize a default dict passed to templates """
    return {
        "title": "",
        "page": "login.tpl",
        "nav": True
    }


@route('/static/<filename:path>')
def static(filename):
    """ return static files """
    return static_file(filename, root="%s/static" % (base))


@route('/')
def index():
    """ index page """
    data = getDataStructure()
    return template('index', page='index', data=data)


@route('/login')
def login():
    """ authentication page """
    data = getDataStructure()
    data["nav"] = False

    user = request.forms.get("user")
    password = request.forms.get("password")

    return template('login', page='login', data=data)


if __name__ == '__main__':

    base = os.path.dirname(os.path.realpath(__file__))

    dom0s = []
    capacity = []

    run(host='localhost', port=8080, reloader=True, debug=True)
