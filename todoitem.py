from config import TODOITEM_FORMAT, DATE_FORMAT

class TodoItem(object):
    """The item of todolist."""
    def __init__(self, id, owner, date, content):
        self.id = id
        self.owner = owner
        self.date = date
        self.content = content
        

    def __repr__(self):
        return "<TodoItem id=%d>" % self.id

    def __str__(self):
        return TODOITEM_FORMAT.format(
            id=self.id, 
            owner=self.owner, 
            date=self.date.strftime(DATE_FORMAT),
            content=self.content
        )
        
