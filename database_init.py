import sqlite3

class Cache:
    def __init__(self) -> None:
        pass

    def update_cache():
        pass
    
with sqlite3.connect('storage.sqlite') as con:
    con.execute('create table if not exists weather ()')