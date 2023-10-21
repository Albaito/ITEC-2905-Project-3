import sqlite3
from datetime import datetime

db = 'storage.sqlite'

class Bookmark:  # class used to receive data from DB
    def __init__(self, climate_forecast=None, POIs=None, id=None):
        self.id = id
        self.climate_forecast = climate_forecast
        self.points_of_interest = POIs
        

    def create_bookmark(self):
        ''' function saves bookmark to database '''
        if self.id == None:
            insert_bookmarks_sql = 'insert into bookmarks (date_retrieved) values (?)'
            with sqlite3.connect('storage.sqlite') as con:
                con.execute(insert_bookmarks_sql, (datetime.now(), ) )
                con.commit()
            con.close()
        else:
            print('Error - Bookmark already in database')

    def add_bookmark_climate_data(self):
        climate_data = self.climate_forecast

        insert_climate_sql = ''' insert into climate (id, day, low, high, precipitation_amount, precipitation_duration) values (?, ?, ?, ?, ?, ?)'''
        counter = 1
        for day in climate_data:
            with sqlite3.connect(db) as con:
                con.execute(insert_climate_sql, (self.id, counter, day.low, day.high, day.precip, day.precip_time) )
            counter += 1
        con.close()

    
    def add_poi_data(self):
        poi_data = self.points_of_interest

        insert_poi_sql = ''' insert into points_of_interests (id, name, city, lattitude, longtitude,) values (?, ?, ?, ?, ?)'''

        for poi in poi_data:
            with sqlite3.connect(db) as con:
                con.execute(insert_poi_sql, (self.id, poi.name, poi.city, poi.lat, poi.long))
                con.commit()
            con.close()


    def delete_bookmark(self):
        if self.id:
            delete_bookmark_sql = 'delete from bookmark where id = ?'

            with sqlite3.connect('storage.sqlite') as con:
                deleted = con.execute(delete_bookmark_sql, (self.id, ) )
                deleted_count = deleted.rowcount
            con.close()

        if deleted_count == 0:
            raise sqlite3.Er
        

