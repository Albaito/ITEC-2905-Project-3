import sqlite3

class Cache:
    def __init__(self) -> None:
        pass

    def update_cache(self):
        if self.id:
            pass
        else:
            pass

    
            
    
with sqlite3.connect('storage.sqlite') as con:
    con.execute('create table if not exists weather (temperature int, weather text, location text)')


def get_all_weather():
    ''' gathers all rows of data from weather table and returns them as objects in a list '''
    get_all_weather_sql = 'select * from weather'

    with sqlite3.connect('storage.sqlite') as con:
        con.row_factory = sqlite3.Row # allows getting of data per column
        cursor = con.cursor()
        rows = cursor.execute(get_all_weather)

        weather_results = []

        for row in rows:

    con.close()

    return rows

