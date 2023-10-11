import datetime
import sqlite3

class Weather:
    def __init__(self, date, temp, id=None, ):
        id = id
        timestamp = date
        temperature = temp

    def update_cache(self):
        if self.id:
            pass
        else:
            pass



    
with sqlite3.connect('storage.sqlite') as con:
    con.execute('create table if not exists weather (temperature int, weather text, location text)')


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

