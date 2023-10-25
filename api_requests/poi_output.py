from poi_api import request_poi
from class_defs import PointOfInterest

def get_name(response, count):
    # not all POIs have a 'name:en' value, so this will pull 'name' if there is a KeyError
    try: 
        poi_name = response['features'][count]['properties']['datasource']['raw']['name:en']
    except KeyError:
        poi_name = response['features'][count]['properties']['datasource']['raw']['name']
    return poi_name

def get_city(response, count):
    poi_city = response['features'][count]['properties']['city']
    return poi_city

def get_lat(response, count):
    poi_lat = response['features'][count]['properties']['lat']
    return poi_lat

def get_long(response, count):
    poi_long = response['features'][count]['properties']['lon']
    return poi_long

def compile_poi_data(location):
    response = request_poi(location)
    response_list = response['features']
    count = 0
    pois = []
    while count < len(response_list):
        name = get_name(response, count)
        city = get_city(response, count)
        lat = get_lat(response, count)
        long = get_long(response, count)
        poi_object = PointOfInterest(name, city, lat, long)
        pois.append(poi_object)
        count = count + 1
    return pois