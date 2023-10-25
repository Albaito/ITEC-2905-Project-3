class ClimateDay:
    def __init__(self, high, low, precip, precip_time):
        self.high = high
        self.low = low
        self.precip = precip
        self.precip_time = precip_time

class PointOfInterest:
    def __init__(self, name, city, lat, long, youtube_id=None, picture_link=None):
        self.name = name
        self.city = city
        self.lat = lat
        self.long = long
        self.youtube_id = youtube_id
        self.picture_link = picture_link

