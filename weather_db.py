import datetime
import sqlite3

db = 'storage.sqlite'

class Weather:  # Placeholder class
    def __init__(self, date, temp, id=None, ):
        id = id
        timestamp = date
        temperature = temp

    def update(self):
        if self.id:
            pass
        else:
            pass

    def save(self):

        insert_weather_sql = 'insert into weather (temperature, weather) VALUES (?, ?, ?)'

        with sqlite3.connect('storage.sqlite') as con:
            con.execute(insert_weather_sql, ())


def create_tables():
    create_table_cache_sql = 'create table if not exists cache (id integer primary key not null, date_retrieved timestamp)'
    create_table_weather_sql = 'create table if not exists weather (id integer, minimum_temperature integer not null, maximum_temperature integer not null, foreign key (id) references cache(id) on delete cascade)'
    create_table_POI_sql = 'create table if not exists point_of_interest (id integer, name text,  lattitude float not null, longtitude float not null, )'

    try:
        with sqlite3.connect(db) as con:
            con.execute(create_table_cache_sql)
            con.execute(create_table_weather_sql)
    except sqlite3.DatabaseError:
        pass # TODO: should raises an error
    finally:
        con.commit()
        con.close()
    
create_tables()

def delete_all_data():
    delete_all_cache_sql = 'delete from cache'
    delete_all_weather_sql = 'delete from weather'

    with sqlite3.connect(db) as con:
        con.executemany(delete_all_cache_sql, delete_all_weather_sql)
        con.commit()
        con.close()
    

def get_all_weather():
    ''' gathers all rows of data from the weather table and returns them as objects in a list '''
    get_all_weather_sql = 'select * from weather'

    with sqlite3.connect('storage.sqlite') as con:
        con.row_factory = sqlite3.Row # allows getting of data per column
        cursor = con.cursor()
        rows = cursor.execute(get_all_weather)

        weather_data = []
        if weather_data:

            for row in rows:
                pass # waiting for data received from API to create objects from table data
        else:
            print('Error - No weather data found')
            return 

    con.close()
    return weather_data

