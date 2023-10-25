'''
This file handles interaction with the database. It has functions to add to the database, view all bookmarks and view individual bookmarks.
'''

from peewee import *
from class_defs_db import *
from class_defs import *

db = SqliteDatabase('basic_ui_db.sqlite')

db.connect()
db.create_tables([ClimateDayDB, PointOfInterestDB, BookmarkDB])

# add bookmark to bookmarks table, return bookmark_id
def add_bookmark(location):
    bookmark = BookmarkDB(location=location)
    bookmark.save()
    return bookmark.id

# add pois to poi table using bookmark_id
def add_pois_to_bookmark(pois, bm_id):
    for i in pois:
        poi = PointOfInterestDB(name=i.name, city=i.city, lat=i.lat, long=i.long, bookmark_id=bm_id)
        poi.save()

# add climate days to climate table using bookmark_id
def add_climate_days_to_bookmark(cds, bm_id):
    for i in cds:
        cd = ClimateDayDB(high=i.high, low=i.low, precip=i.precip, precip_time=i.precip_time, bookmark_id=bm_id)
        cd.save()

# return all bookmarks
def view_all_bookmarks():
    bookmarks = BookmarkDB.select()
    return bookmarks

# get climate data using bookmark_id
def get_bookmark_climate(id):
    climate_list = []
    bookmark_climate = ClimateDayDB.select().where(ClimateDayDB.bookmark_id == id)
    for i in bookmark_climate:
        day_object = ClimateDay(i.high, i.low, i.precip, i.precip_time)
        climate_list.append(day_object)
    return climate_list

# get poi data using bookmark_id
def get_bookmark_poi(id):
    poi_list = []
    bookmark_poi = PointOfInterestDB.select().where(PointOfInterestDB.bookmark_id == id)
    for i in bookmark_poi:
        poi_object = PointOfInterest(i.name, i.city, i.lat, i.long)
        poi_list.append(poi_object)
    return poi_list