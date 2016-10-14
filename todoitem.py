from config import TODOITEM_FORMAT, DATE_FORMAT

class TodoItem(object):
    """The item of todolist."""
    def __init__(self, id, owner, date, state, content):
        self.id = id
        self.owner = owner
        self.date = date
        self.state = state
        self.content = content
        
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str((self.id, self.owner, self.date.strftime(DATE_FORMAT),
            self.state, self.content))
        
