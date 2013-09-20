#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import bottle
from bottle import route, run, template, static_file, get, post
from bottle import request, error, hook


@route('/static/<filename:path>')
def static(filename):
    """ return static files """
    return static_file(filename, root="%s/static" % (base))


@route('/login')
def login():
    data = {}
    return template('login', page='login', data=data)


@route('/buttons')
def buttons():
    data = {}
    return template('buttons', page='buttons', data=data)


@route('/calendar')
def calendar():
    data = {}
    return template('calendar', page='calendar', data=data)


@route('/editors')
def editors():
    data = {}
    return template('editors', page='editors', data=data)


@route('/form')
def form():
    data = {}
    return template('form', page='form', data=data)


@route('/interface')
def interface():
    data = {}
    return template('interface', page='interface', data=data)


@route('/stats')
def stats():
    data = {}
    return template('stats', page='stats', data=data)


@route('/tables')
def tables():
    data = {}
    return template('tables', page='tables', data=data)


@route('/')
@route('/index')
def index():
    data = {}
    return template('index', page='index', data=data)


if __name__ == '__main__':

    """ get base application path """
    base = os.path.dirname(os.path.realpath(__file__))

    app = bottle.app()
    bottle.run(
        app=app,
        host='37.187.6.69',
        port=80,
        reloader=True,
        debug=True
    )
