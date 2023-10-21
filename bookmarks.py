import sqlite3
from datetime import datetime

class Bookmark:  # Placeholder class
    def __init__(self, climate_forecast, POIs=None, id=None):
        self.id = id
        self.climate_forecast = climate_forecast
        self.points_of_interest = POIs
        

    def add_bookmark(self):
        ''' function saves bookmark to database '''
        if self.id == None:
            insert_bookmarks_sql = 'insert into bookmarks (date_retrieved) values (?)'
            insert_climate_sql = ' insert into climate (id, day, low, high, precipitation_amount, precipitation_duration) values (?, ?, ?, ?, ?)'
            insert_POIs_sql = ' insert into point_of_interests (id, name, city, lattitude, longtitude, link, picture_link, video_link) values (?, ?, ?, ?, ?, ?, ?)'
            with sqlite3.connect('storage.sqlite') as con:
                con.execute(insert_bookmarks_sql, (datetime.now(), ) )
                con.execute(insert_climate_sql, () )
            con.close()
        else:
            print('')


    def delete_bookmark(self):
        if self.id:
            delete_bookmark_sql = 'delete from bookmark where id = ?'

            with sqlite3.connect('storage.sqlite') as con:
                deleted = con.execute(delete_bookmark_sql, (self.id, ) )
                deleted_count = deleted.rowcount
            con.close()

        if deleted_count == 0:
            raise sqlite3.Er
        
print(datetime.now())
        
