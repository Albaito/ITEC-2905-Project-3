class Bookmark:  # Placeholder class
    def __init__(self, date, min_temp, max_temp, id=None, ):
        id = id
        date = date
        minimum_temperature = min_temp
        maximum_temperature = max_temp

    def update(self):
        if self.id:
            pass
        else:
            pass

    def save(self):

        insert_weather_sql = 'insert into weather (temperature, weather) VALUES (?, ?, ?)'

        with sqlite3.connect('storage.sqlite') as con:
            con.execute(insert_weather_sql, (self))