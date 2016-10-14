from todolist import TodoList
from todoitem import TodoItem
from user import User
from datetime import datetime

u = User("David")
obj = TodoItem(1, u, datetime.now(), "hello world!")
obj2 = TodoList(obj)

print obj