import sqlite3
from bookmarks import Bookmark

db = 'storage.sqlite'

def create_tables():
    create_table_bookmark_sql = 'create table if not exists bookmarks (id integer primary key not null, date_retrieved timestamp)'
    create_table_climate_sql = 'create table if not exists climate (id integer, minimum_temperature integer not null, maximum_temperature integer not null, weather text not null, foreign key (id) references cache(id) on delete cascade)'
    create_table_POI_sql = 'create table if not exists point_of_interests (id integer, name text,  lattitude float not null, longtitude float not null, link1 text, picture_link2 text, video_link text, foreign key (id) references caches(id) on delete cascade)'
    create_table_sql_statments = [create_table_bookmark_sql, create_table_climate_sql, create_table_POI_sql]

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
    get_all_bookmarks_sql = 'select * from bookmarks, climate, point_of_interests'

    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            rows = cur.execute(get_all_bookmarks_sql)
        
        bookmarks = [r['minimum_temperature',]]

        for r in rows:
            Bookmark(r[''])
    except sqlite3.DataError:
        print('Uh oh')
    finally:
        con.close()
        return bookmarks

def delete_all_data():
    delete_all_cache_sql = 'delete from bookmarks'

    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute(delete_all_cache_sql)
    except Exception as e:
        print(e)
    finally:
        con.commit()
        con.close()  

def insert_new_row():
    ''' Function inserts  '''
    insert_row_sql = 'insert into cache values(?, ?),'

def get_all_climate_data():
    ''' gathers all rows of data from the climate table and returns them as objects in a list '''
    get_all_climate_data_sql = 'select * from climate'

    with sqlite3.connect('storage.sqlite') as con:
        con.row_factory = sqlite3.Row # allows getting of data per column
        cursor = con.cursor()
        rows = cursor.execute(get_all_climate_data)

        climate_data = []
        if climate_data:

            for row in rows:
                pass # waiting for data received from API to create objects from table data
        else:
            print('Error - No climate data found')
            return 

    con.close()
    return climate_data

get_all_bookmarks()
