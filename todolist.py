from todoitem import TodoItem
from config import TODOLIST_FORMAT

class TodoList(object):
    """The list of the todo items as well as the main struct in this object."""
    def __init__(self, username, *items):
        self.user = username
        self.items = list(items)
        
    def __str__(self):
        return str((self.user, self.items))
        
    def add_item(self, item):
        self.items.append(item)