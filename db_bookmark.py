import sqlite3

db = 'storage.sqlite'

def create_tables():
    create_table_bookmark_sql = 'create table if not exists bookmarks (id integer primary key not null, date_retrieved timestamp)'
    create_table_weather_sql = 'create table if not exists weather (id integer, minimum_temperature integer not null, maximum_temperature integer not null, weather text not null, foreign key (id) references cache(id) on delete cascade)'
    create_table_POI_sql = 'create table if not exists point_of_interest (id integer, name text,  lattitude float not null, longtitude float not null, link1 text, picture_link2 text, video_link text, foreign key (id) references caches(id) on delete cascade)'
    create_table_sql_statments = [create_table_bookmark_sql, create_table_weather_sql, create_table_POI_sql]

    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            for sql_statment in create_table_sql_statments:
                cur.execute(sql_statment)
    except sqlite3.DatabaseError:
        pass # TODO: should raises an error
    finally:
        con.commit()
        con.close()
    
create_tables()

def get_all_bookmarks():
    sget_all_bookmarks_sql = 'select * from bookmark'

def delete_all_data():
    delete_all_cache_sql = 'drop table if exists cache'

    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute(delete_all_cache_sql)
    except Exception as e:
        print(e)
    finally:
        con.commit()
        con.close()

delete_all_data()    

def insert_new_row():
    ''' Function inserts  '''
    insert_row_sql = 'insert into cache values(?, ?),'

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

