import codecs
import json
import os, sys

class Storage(object):
    """The Todolist Storage Class."""
    def __init__(self, data_addr):
        self.data_addr = data_addr
        self.data = []
        self.read_from_file()

    def is_valid_user(self, username):
        return self._storage.is_valid_user(username)

    def read_from_file(self):
        if not os.path.exists(self.data_addr):
            return None # do nothing
        with codecs.open(self.data_addr, encoding="utf-8") as f:
            self.data = json.load(f, encoding="utf-8")
        
    def write_to_file(self):
        with codecs.open(self.data_addr, encoding="utf-8") as f:
            json.dump(f, encoding='utf-8')

    def sync(self):
        self.write_to_file()
