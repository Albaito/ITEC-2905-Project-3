'''
This file defines the models for the peewee database app.
'''

from peewee import *

db = SqliteDatabase('basic_ui_db.sqlite')

# bookmark model
class BookmarkDB(Model):
    location = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.location}'
    
# climate model
class ClimateDayDB(Model):
    high = FloatField()
    low = FloatField()
    precip = FloatField()
    precip_time = FloatField()
    bookmark_id = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.high}, {self.low}, {self.precip}, {self.precip_time}'
    
# poi model
class PointOfInterestDB(Model):
    name = CharField()
    city = CharField()
    lat = FloatField()
    long = FloatField()
    bookmark_id = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name}, {self.city}, {self.lat}, {self.long}'
    
# youtube model
class YouTubeDB(Model):
    title = CharField()
    id = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.title}, {self.id}'