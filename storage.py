import codecs
import json
import os, sys
from todolist import TodoList
from config import DATE_FORMAT


class TodoListEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, TodoList):
            return json.dumps([o.user, [[i.id, i.owner, i.date.strftime(DATE_FORMAT),
                i.state, i.content] for i in o.items]])
        return json.JSONEncoder.default(self, o)

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
                result = json.load(f, encoding="utf-8")
            except ValueError:
                print "Parsing Failed"
                raise
            else:
                self.data = result
        
    def write_to_file(self):
        with open(self.data_addr, "wt") as f:
            try:
                content = json.dumps(self.data, encoding='utf-8', cls=TodoListEncoder)
            except TypeError as err:
                print err
                raise
            else:
                f.write(content)

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
