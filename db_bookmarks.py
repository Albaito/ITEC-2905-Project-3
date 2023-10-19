import sqlite3
from bookmarks import Bookmark
from api_requests.class_defs import PointOfInterest

db = 'storage.sqlite'

def create_tables():
    create_table_bookmark_sql = 'create table if not exists bookmarks (id integer primary key not null)'
    create_table_climate_sql = 'create table if not exists climate (id integer, day int, low integer not null, high integer not null, precipitation_amount float, precipitation_duration float, foreign key (id) references cache(id) on delete cascade)'
    create_table_POI_sql = 'create table if not exists point_of_interests (id integer, name text, city text not null, lattitude float not null, longtitude float not null, link text, picture_link text, video_link text, foreign key (id) references caches(id) on delete cascade)'
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
    get_all_bookmarks_sql = 'select id, day, low, high, precipitation_amount, precipitation_duration, name, city, lattitude, longtitude, link, climate, picture_link, video_link from bookmarks join climate on bookmarks.id = climate.id join point_of_interests on bookmarks.id = climate.id'

    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            rows = cur.execute(get_all_bookmarks_sql)
        
        bookmarks = []

        for row in rows:
            bookmark = Bookmark(row['low'], row['high'], row['precipitation_amount'], row['precipitation_duration'])
            bookmark.id = row['id']
    
            POIS = get_POIs_by_id(bookmark.id)
            bookmark.POI1 = POIS[0]
            bookmark.POI2 = POIS[1]
            bookmark.POI3 = POIS[2]
            bookmark.POI4 = POIS[3]
            bookmark.POI5 = POIS[4] # There should always be 5 POIs per location so this seemed simpler than a 3 tiered solution
            # This probably couldbe done with a for each loop, but need to get it done

            bookmarks.append(bookmark)
    except sqlite3.DataError:
        print('Uh oh')
    finally:
        con.close()
        return bookmarks


def get_POIs_by_id(id):
    get_POI_by_id_sql = ''' select * from point_of_interests wheere id = ? '''

    con = open_db_connection()

    rows = con.execute(get_POI_by_id_sql, (id ,) )

    poi_list = []
    for row in rows:
        point_of_interest = PointOfInterest(row['name'], row['city'], row['lattitude'], row['longtitude'], row['lattitude'])
        poi_list.append(point_of_interest)
    con.close()
    return poi_list


def get_all_POIs():
    get_all_POIs_sql = 'select * from point_of_interests order by id' 

    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            rows = cur.execute(get_all_POIs_sql)

            pois = []

            for row in rows:
                point_of_interest = PointOfInterest(row['name'], row['city'], row['lattitude'], row['longtitude'], row['id'])
                pois.append(point_of_interest)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return pois
    


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

def open_db_connection():
    try:
        db = 'storage.sqlite'

        con = sqlite3.connect(db)

    except sqlite3.DatabaseError:
        print(f'Error - Database: {db} is missing')
    finally:
        return con



print(get_all_bookmarks())
