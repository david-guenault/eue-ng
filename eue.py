#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from beaker.middleware import SessionMiddleware
import bottle
from bottle import route, run, template, static_file, get, post, request
from lib import eueauth, euemongo


def getDataStructure():
    """ initialize a default dict passed to templates """
    return {
        "title": "",
        "page": "login.tpl",
        "nav": True,
        "message": {
            "type": "",
            "content": ""
        }
    }


@route('/static/<filename:path>')
def static(filename):
    """ return static files """
    return static_file(filename, root="%s/static" % (base))


@route('/')
def index():
    """ check if session is active """
    if auth:
        if not auth.session["isAuth"]:
            redirect("/login")
    else:
        redirect("/login")

    """ index page """
    data = getDataStructure()
    return template('index', page='index', data=data)


@route('/login')
def login():
    """ authentication page """
    data = getDataStructure()
    data["nav"] = False

    return template('login', page='login', data=data)


@route('/logout')
def logout():
    """ logout process """
    data = getDataStructure()
    data["nav"] = False

    auth.logout()

    redirect("/login")


@post('/do_login')
def do_login():
    """ process login check """
    data = getDataStructure()
    data["nav"] = False

    user = request.forms.get("user")
    password = request.forms.get("password")

    if not auth.login(user, password):
        return template('login', page='login', data=data)
    else:
        redirect("/")

if __name__ == '__main__':

    mongohost = "localhost"
    monogoport = 27017
    mongodb = "eue"
    mongousercollection = "users"

    """ get base application path """
    base = os.path.dirname(os.path.realpath(__file__))

    """ create an instance of mongo db connection class """

    mongo = euemongo.mongo(mongohost, monogoport, mongodb)
    mongo.connect()

    """ create an instance of authentication lib """
    auth = eueauth.auth(mongo, "users")

    """ create a bottle app with beaker session support """
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': '%s/sessions' % base,
        'session.auto': True
    }

    """
        host='localhost',
        port=8080,
        reloader=True,
        debug=True
    """

    myapp = SessionMiddleware(bottle.app(), session_opts)
    run(app=myapp)
