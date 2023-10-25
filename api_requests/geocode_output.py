from geocode_api import request_geocode

def get_latitude(response):
    lat = response['results'][0]['latitude']
    return lat

def get_longitude(response):
    long = response['results'][0]['longitude']
    return long

def get_timezone(response):
    try:
        tz = response['results'][0]['timezone']
    except KeyError:
        tz = 'Europe/London'
    return tz

def compile_geocode_data(location):
    response = request_geocode(location)
    lat = get_latitude(response)
    long = get_longitude(response)
    tz = get_timezone(response)
    return lat, long, tz

def geocode_validation(location):
    response = request_geocode(location)
    if len(response) == 1:
        return True
    else:
        return False