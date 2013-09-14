#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from beaker.middleware import SessionMiddleware
import bottle
from bottle import route, run, template, static_file, get, post, request, error
from lib import eueauth, euemongo, eueuser


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


def getSessionStructure():
    """ return an empty session dict """
    return {
        "isAuth": False,
        "email": ""
    }


def isAuth():
    """ check if session is active """
    isAuth = False
    s = bottle.request.environ.get('beaker.session')

    if "auth" in s:
        if s["auth"]["isAuth"]:
            isAuth = True

    return isAuth


def redirectWithMessage(redirectTo, messageType,
                        messageContent, additonalData=None):
    """ not a real redirect but display a template with message """
    data = getDataStructure()

    for key in additonalData:
        data[key] = additonalData[key]

    data["message"] = {
        "type": messageType,
        "content": messageContent}
    return template(redirectTo, page=redirectTo, data=data)


@error(404)
def error_route(code):
    """ 404 error page """
    data = getDataStructure()
    data["nav"] = False
    return template("error", page="error", data=data)


@route('/static/<filename:path>')
def static(filename):
    """ return static files """
    return static_file(filename, root="%s/static" % (base))


@route('/profile')
def profile():
    """ profile page """
    data = getDataStructure()
    if not isAuth():
        return redirectWithMessage(
            "login",
            "danger",
            "You must be logged in to access this page",
            {"nav": False})
    else:
        s = bottle.request.environ.get('beaker.session')
        data["profile"] = user.get(s['auth']["email"])
        fields = ["email", "password", "firstname", "lastname"]
        for field in fields:
            if not field in data["profile"]:
                data["profile"][field] = ""
        return template('profile', page='profile', data=data)


@route('/profile_update')
def profile_update():
    """ update user profile """
    data = getDataStructure()
    if not isAuth():
        return redirectWithMessage(
            "login",
            "danger",
            "You must be logged in to access this page",
            {"nav": False})
    else:
        fields = ["email", "password", "firstname", "lastname"]
        profile = {}
        for field in fields:
            if field == "password":
                if request.forms.get(field) != "":
                    profile[field] = request.forms.get(field)
            else:
                profile[field] = request.forms.get(field)

        result = user.update(profile)

        return template('profile', page='profile', data=data)


@route('/')
def index():
    """ index page """
    if not isAuth():
        return redirectWithMessage(
            "login",
            "danger",
            "You must be logged in to access this page",
            {"nav": False})
    else:
        data = getDataStructure()
        return template('index', page='index', data=data)


@route('/login')
def login():
    """ login page """
    data = getDataStructure()
    data["nav"] = False
    return template('login', page='login', data=data)


@route('/logout')
def logout():
    """ logout process """
    s = bottle.request.environ.get('beaker.session')
    s['auth'] = getSessionStructure()
    data = getDataStructure()
    data["nav"] = False
    bottle.redirect("/login")


@post('/do_login')
def do_login():
    """ process login check """
    data = getDataStructure()
    data["nav"] = False

    user = request.forms.get("user")
    password = request.forms.get("password")

    if len(user) > 0 and len(password) > 0:
        if auth.login(user, password):
            s = bottle.request.environ.get('beaker.session')
            s['auth'] = getSessionStructure()
            s['auth']['isAuth'] = True
            s['auth']['email'] = user
            bottle.redirect("/")
        else:
            return redirectWithMessage(
                "login",
                "danger",
                "Invalid user name and/or password",
                {"nav": False})
    else:
        return redirectWithMessage(
            "login",
            "danger",
            "User and password are mandatory",
            {"nav": False})

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

    """ create an instance of user lib """
    user = eueuser.user(mongo, "users")

    """ create an instance of authentication lib """
    auth = eueauth.auth(mongo, "users")

    """ create a bottle app with beaker session support """
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': '%s/sessions' % base,
        'session.auto': True
    }

    myapp = SessionMiddleware(bottle.app(), session_opts)
    bottle.run(
        app=myapp,
        host='localhost',
        port=8080,
        reloader=True,
        debug=True
    )
