import sqlite3

class Bookmark:  # Placeholder class
    def __init__(self, date, min_temp, max_temp, id=None, ):
        id = id
        date = date
        minimum_temperature = min_temp
        maximum_temperature = max_temp

    def update(self):
        if self.id:
            pass # TODO: should return with message saying bookmark is already in DB
        else:
            self.add_bookmark(self)

    def add_bookmark(self):
        ''' function saves bookmark to database '''
        insert_weather_sql = 'insert into weather (temperature, weather) VALUES (?, ?, ?)'

        with sqlite3.connect('storage.sqlite') as con:
            con.execute(insert_weather_sql, (self))
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
