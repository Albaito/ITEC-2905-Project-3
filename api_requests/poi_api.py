import requests
import os
from pprint import pprint

api_key = '5340049be7ae4777912c67530c66487b'
poi_url = 'https://api.geoapify.com/v2/places'

poi_categories = 'tourism.sights,tourism.attraction,tourism.information'
poi_location = 'circle:-93.2638,44.96,5000'


def request_poi(location):
    poi_query = {'categories': poi_categories, 'filter': location, 'limit': 5, 'apiKey': api_key}
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







