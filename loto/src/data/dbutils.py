import shelve

from settings import DATA_DB_FILE

db = None

def open():
    global db
    if db is None:
        db = shelve.open(DATA_DB_FILE)
    return db

def close():
    global db
    db.close()
    db = None