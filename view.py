#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""The Viewer in TodoList by bottle."""

import config
from config import ROOT_DIR, STATIC_DIR, STATE_UNDO, STATE_DONE
import config
from bottle import route, static_file, Bottle, template, error, redirect
from user import User
from todoitem import TodoItem
from todolist import TodoList
from service import Service
from datetime import datetime
from random import randint

app = Bottle()
service = Service()

service.load()

@app.route('/<username>')
def UI(username):
    if not service.is_valid_user(username):
        return "Please Register!"
    tdl = service.get_todolist(username)
    print tdl
    return template("templates/index.html", todolist=tdl, config=config)
'''
@app.route('/')
@app.route('/index.html')
def index():
    u = User("sysuAT")
    items = [TodoItem(i, u, datetime.now(), STATE_UNDO,str(randint(0, 1234567))) for i in xrange(20)]
    tdl = TodoList(u, *items)
    return template("templates/index.html", todolist=tdl)
'''

@app.route('/static/<files:path>')
def return_static_files(files):
    print files
    return static_file('static/' + files, root=ROOT_DIR)


@app.route('/<username>/do/<id:int>')
def echo(username, id):
    if not service.is_valid_user(username):
        return None
    service.do_item(username, id)
    return redirect('/' + username)


@app.route('/<username>/undo/<id:int>')
def echo(username, id):
    if not service.is_valid_user(username):
        return None
    service.undo_item(username, id)
    return redirect('/' + username)


@error(404)
def error404(error):
    return 'Nothing here, sorry'

app.run(debug=True, reload=True, port=8888)
