#!/usr/bin/env python
from todolist import TodoList
from todoitem import TodoItem
from user import User
from service import Service
from datetime import datetime
from config import STATE_UNDO, STATE_DONE


service = Service()


service.add_user('David')
service.add_user('Tiiiiiiiiim')
service.add_user('Jack')

service.add_todoitem('David', TodoItem(1, 'David', datetime.now(), STATE_UNDO, "Hello I am David!"))
service.add_todoitem('David', TodoItem(2, 'David', datetime.now(), STATE_UNDO, "Hello I am David!"))
service.add_todoitem('Jack', TodoItem(3, 'Jack', datetime.now(), STATE_UNDO, "I am Jack, I hate you, David!"))

service.save()