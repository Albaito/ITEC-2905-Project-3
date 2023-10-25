'''
This file defines the class definitions used to output the lookup function tables.
'''

# class for climate days
class ClimateDay:
    def __init__(self, high, low, precip, precip_time):
        self.high = high
        self.low = low
        self.precip = precip
        self.precip_time = precip_time

# class for points of interest
class PointOfInterest:
    def __init__(self, name, city, lat, long):
        self.name = name
        self.city = city
        self.lat = lat
        self.long = long