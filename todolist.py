from todoitem import TodoItem
from config import TODOLIST_FORMAT

class TodoList(object):
    """The list of the todo items as well as the main struct in this object."""
    def __init__(self, user, *items):
        self.user = user
        self.items = list(items)
        
    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return "<TodoList user=%r>" % self.user
        