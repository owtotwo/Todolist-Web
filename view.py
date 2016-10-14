#-*- coding:utf-8 -*-

"""The Viewer in TodoList by bottle."""

from config import ROOT_DIR, STATIC_DIR
from bottle import route, static_file, Bottle, template, error
from user import User
from todoitem import TodoItem
from todolist import TodoList
from datetime import datetime
from random import randint

app = Bottle()

@app.route('/')
@app.route('/index.html')
def index():
    u = User("sysuAT")
    items = [TodoItem(i, u, datetime.now(), str(randint(0, 1234567))) for i in xrange(20)]
    tdl = TodoList(u, *items)
    return template("templates/index.html", todolist=tdl)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

app.run(debug=True)