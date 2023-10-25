'''
This file calls the Geoapify API to get information on nearby points of interest. It returns the top 5 nearby POIs.
'''

import requests
import os
from geocode_output import compile_geocode_data

api_key = os.environ.get('GEOAPIFY_KEY')
poi_url = 'https://api.geoapify.com/v2/places'

poi_categories = 'tourism.sights,tourism.attraction,tourism.information'

# build string with geocode data
def build_location_string(location):
    latitude, longitude, timezone = compile_geocode_data(location)
    radius = 5000
    location_string = f'circle:{longitude},{latitude},{radius}'
    return location_string

# call POI api
def request_poi(location):
    location_string = build_location_string(location)
    poi_query = {'categories': poi_categories, 'filter': location_string, 'limit': 5, 'apiKey': api_key}
    try:
        poi_response = requests.get(poi_url, params=poi_query)
        poi_response.raise_for_status()
        return poi_response.json()
    
    except Exception as e:
        print(e)