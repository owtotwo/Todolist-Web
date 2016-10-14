#!/usr/bin/env python
from todolist import TodoList
from todoitem import TodoItem
from user import User
from datetime import datetime
from config import STATE_UNDO, STATE_DONE

u = User("David")
obj = TodoItem(1, u, datetime.now(), STATE_UNDO, "hello world!")
obj2 = TodoList(obj)

print obj