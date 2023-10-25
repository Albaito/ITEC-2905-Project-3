import sqlite3
from bookmarks import Bookmark
from api_requests.class_defs import PointOfInterest
from api_requests.class_defs import ClimateDay

db = 'storage.sqlite'

def create_tables():
    create_table_bookmark_sql = 'create table if not exists bookmarks (id integer primary key not null, date_retrieved string not null)'
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
            bookmark = Bookmark()
            bookmark.id = row['id']
    
            points_of_interest = get_POIs_by_id(bookmark.id)  # Iterable list to loop through POis
            bookmark.points_of_interest = points_of_interest

            climate_forecast = get_climate_by_id(bookmark.id)   # Iterable list to loop through climate data
            bookmark.climate_forecast = climate_forecast

            bookmarks.append(bookmark)
    except sqlite3.DataError:
        print('Uh oh')
    finally:
        con.close()
        return bookmarks


def get_climate_by_id(id):
    get_climate_by_id_sql = ''' select * from climate where id = ? order by day'''

    con = open_db_connection()

    rows = con.execute(get_climate_by_id_sql, (id ,) )

    days = []
    for row in rows:
        day = ClimateDay(row['high'], row['low'], row['precipitation_amount'], row['precipitation_duration'])
        days.append(day)
    con.close()

    return days


def get_POIs_by_id(id):
    get_POI_by_id_sql = ''' select * from point_of_interests wheere id = ? order by name'''

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
                point_of_interest.youtube_id = row['video_link']
                point_of_interest.picture_link = row['picture_link']
                pois.append(point_of_interest)
    except Exception as e:
        print(e)
    finally:
        con.close()
        return pois
    


def delete_all_data():
    ''' function deletes all rows in bookmarks table which cascades to climate and points_of_interest'''
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
    get_all_climate_data_sql = 'select * from climate order by id'

    with sqlite3.connect('storage.sqlite') as con:
        con.row_factory = sqlite3.Row # allows getting of data by column
        cursor = con.cursor()
        rows = cursor.execute(get_all_climate_data_sql)

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
    ''' opens database connection 
    and returns a connection object'''
    try:
        db = 'storage.sqlite'

        con = sqlite3.connect(db)

    except sqlite3.DatabaseError:
        print(f'Error - Database: {db} is missing!')
    finally:
        return con