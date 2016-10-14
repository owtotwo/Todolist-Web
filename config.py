import os
ROOT_DIR = os.getcwd()
STATIC_DIR = os.path.join(ROOT_DIR, "static/")
TODOITEM_FORMAT = "{id:<3} {owner:<10} {date:<18} {state:<}\n{content}\n"
DATE_FORMAT = "%Y-%m-%d/%H:%M"
TODOLIST_FORMAT = ""
STATE_UNDO = "Undo"
STATE_DONE = "Done"