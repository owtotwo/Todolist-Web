from storage import Storage
from config import DATA_FILE

class Service(object):
    """The Todolist Service Class."""
    def __init__(self):
        self._storage = Storage(DATA_FILE)

    def is_valid_user(self, username):
        return self._storage.is_valid_user(username)