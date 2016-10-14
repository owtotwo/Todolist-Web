class User(object):
    """The user class of the Todolist."""
    def __init__(self, name):
        self.name = name
        self._ip_addr = None # do something

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<User %r>" % self.name