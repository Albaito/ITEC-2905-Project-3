import requests
import os
from geocode_output import compile_geocode_data

api_key = os.environ.get('GEOAPIFY_KEY')
poi_url = 'https://api.geoapify.com/v2/places'

poi_categories = 'tourism.sights,tourism.attraction,tourism.information'
poi_location = 'berlin'

# build string with geocode data
def build_location_string(location):
    latitude, longitude, timezone = compile_geocode_data(location)
    radius = 5000
    location_string = f'circle:{longitude},{latitude},{radius}'
    return location_string


def request_poi(location):
    location_string = build_location_string(location)
    poi_query = {'categories': poi_categories, 'filter': location_string, 'limit': 5, 'apiKey': api_key}
    try:
        poi_response = requests.get(poi_url, params=poi_query)
        poi_response.raise_for_status()
        return poi_response.json()
    
    except Exception as e:
        print(e)

def main():
    response = request_poi(poi_location)
    pprint(response)

main()