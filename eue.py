#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from beaker.middleware import SessionMiddleware
import bottle
from bottle import route, run, template, static_file, get, post
from bottle import request, error, hook
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


def getSession():
    """ get session structure """
    s = bottle.request.environ.get('beaker.session')
    return s


def closeSession():
    """ and a session and redirect to login page """
    session = getSession()
    session["auth"] = getSessionStructure()


def getSessionStructure():
    """ return an empty session dict """
    return {
        "isAuth": False,
        "email": ""
    }


def isAuth():
    session = getSession()
    """ check if session is active """
    isAuth = False

    if "auth" in session:
        if session["auth"]["isAuth"]:
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


# @error(404)
# @error(500)
# @error(405)
# def error_route(code):
#     """ XXX error page """
#     data = getDataStructure()
#     data["nav"] = False
#     data["error"] = {}
#     data["error"]["code"] = code or "500"
#     data["error"]["reason"] = "An error occured while processing the page"
#     data["error"]["description"] = ""
#     return template("error", page="error", data=data)

@route('/static/<filename:path>')
def static(filename):
    """ return static files """
    return static_file(filename, root="%s/static" % (base))


@route('/profile')
def profile():
    session = getSession()
    """ profile page """
    data = getDataStructure()
    if not isAuth():
        return redirectWithMessage(
            "login",
            "danger",
            "You must be logged in to access this page",
            {"nav": False})
    else:
        data["profile"] = user.get(session['auth']["email"])
        if not data["profile"]:
            redirectWithMessage(redirectTo="login",
                                messageType="warning",
                                messageContent="Session expired")
        """ fill in profile structure """
        fields = ["email", "password", "firstname", "lastname"]
        for field in fields:
            if not field in data["profile"]:
                data["profile"][field] = ""
        return template('profile', page='profile', data=data)


@post('/profile_update')
def profile_update():
    session = getSession()
    """ update user profile """
    data = getDataStructure()
    if not isAuth():
        return redirectWithMessage(
            "profile_update",
            "danger",
            "You must be logged in to access this page",
            {"nav": False})
    else:
        profile = user.get(session["auth"]["email"])

        email = session["auth"]["email"]
        password = request.forms.get("password")
        firstname = request.forms.get("firstname")
        lastname = request.forms.get("lastname")

        profile = {"email": email,
                   "firstname": request.forms.get("firstname"),
                   "lastname": request.forms.get("lastname")}

        if len(password) > 0:
            profile["password"] = password

        data["profile"] = profile

        result = user.update(profile)

        data["profile"] = profile

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
    """ close a session and redirect to login """
    closeSession()
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


@route("/users")
def users():
    """ users management page """
    if not isAuth():
        return redirectWithMessage(
            "login",
            "danger",
            "You must be logged in to access this page",
            {"nav": False})
    else:
        data = getDataStructure()
        return template('users', page='users', data=data)

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
        'session.auto': True,
        'session.persist': True
    }

    myapp = SessionMiddleware(bottle.app(), session_opts)

    bottle.run(
        app=myapp,
        host='localhost',
        port=8080,
        reloader=True,
        debug=True
    )
