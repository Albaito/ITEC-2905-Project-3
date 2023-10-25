'''
This file processes the Geocode API response. It extracts latitude, longitude and timezone from the JSON response.
It also handles some input validation by checking that the response returns usable data.
'''

from geocode_api import request_geocode

# extract latitude
def get_latitude(response):
    lat = response['results'][0]['latitude']
    return lat

# extract longitude
def get_longitude(response):
    long = response['results'][0]['longitude']
    return long

# extract timezone
def get_timezone(response):
    try:
        tz = response['results'][0]['timezone']
    except KeyError:
        tz = 'Europe/London'
    return tz

# compile and return geocode data
def compile_geocode_data(location):
    response = request_geocode(location)
    lat = get_latitude(response)
    long = get_longitude(response)
    tz = get_timezone(response)
    return lat, long, tz

# invalid geocode results return JSON containing a single element
# if the response length is 1, the location input is invalid
def geocode_validation(location):
    response = request_geocode(location)
    if len(response) == 1:
        return True
    else:
        return False