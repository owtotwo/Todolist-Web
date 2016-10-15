import codecs
import json
import os, sys
from todolist import TodoList
from todoitem import TodoItem
from config import DATE_FORMAT, STATE_DONE, STATE_UNDO
from datetime import datetime


class TodoListEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TodoList):
            return [obj.user, [[i.id, i.owner, i.date.strftime(DATE_FORMAT),
                i.state, i.content] for i in obj.items]]
        return json.JSONEncoder.default(self, obj)


def as_todolist(obj):
    if isinstance(obj, dict):
        tdl_list = {}
        for k, v in obj.items():
            items = [TodoItem(i[0], i[1], datetime.strptime(i[2], DATE_FORMAT),
                     i[3], i[4]) for i in v[1]]
            tdl_list[k] = TodoList(v[0], *items)
        return tdl_list
    return obj


class Storage(object):
    """The Todolist Storage Class."""
    def __init__(self, data_addr):
        self.data_addr = data_addr
        self.data = {}

    def is_valid_user(self, username):
        return self._storage.is_valid_user(username)

    def read_from_file(self):
        if not os.path.isfile(self.data_addr):
            return None # do nothing
        with open(self.data_addr, "rt") as f:
            try:
                result = json.load(f, encoding="utf-8", object_hook=as_todolist)
            except ValueError:
                print "Parsing Failed"
                raise
            else:
                self.data = result
        
    def write_to_file(self):
        with open(self.data_addr, "wt") as f:
            try:
                json.dump(self.data, f, encoding='utf-8', cls=TodoListEncoder,
                          indent=4, sort_keys=True, separators=(',', ':'))
            except TypeError as err:
                print err
                raise

    def sync(self):
        self.write_to_file()

    def add_user(self, username):
        self.data[username] = TodoList(username)

    def add_todoitem(self, username, item):
        self.data[username].add_item(item)

    def get_todolist(self, username):
        try:
            return self.data[username]
        except KeyError:
            raise

    def is_valid_user(self, username):
        return username in self.data

    def do_item(self, username, item_id):
        for item in self.data[username].items:
            if item.id == item_id:
                item.state = STATE_DONE
                return True
        else:
            print "ID Not Found"
            return False

    def undo_item(self, username, item_id):
        for item in self.data[username].items:
            if item.id == item_id:
                item.state = STATE_UNDO
                return True
        else:
            print "ID Not Found"
            return False