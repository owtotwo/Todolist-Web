from storage import Storage
from config import DATA_FILE

class Service(object):
    """The Todolist Service Class."""
    def __init__(self):
        self._storage = Storage(DATA_FILE)

    def is_valid_user(self, username):
        return self._storage.is_valid_user(username)

    def get_todolist(self, username):
        self._storage.get_todolist(username)

    def add_user(self, username):
        self._storage.add_user(username)

    def add_todoitem(self, username, item):
        self._storage.add_todoitem(username, item)

    def sync(self):
        self._storage.sync()