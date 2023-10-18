from poi_api import request_poi
from pprint import pprint
from class_defs import PointOfInterest

location = 'berlin'

# def get_response(location):
#     response = request_poi(location)
#     return response

def get_name(response, count):
    poi_name = response['features'][count]['properties']['datasource']['raw']['name:en']
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

def compile_data(location):
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
    
def main():
    poi_list = compile_data('berlin')
    print(poi_list)
    for i in poi_list:
        print(i.name)
        print(i.city)
        print(i.lat)
        print(i.long)

main()



# test_response = get_response(location)
# test_name = get_name(test_response, 0)

# print(test_name)