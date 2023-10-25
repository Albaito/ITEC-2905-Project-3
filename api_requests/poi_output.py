from poi_api import request_poi
from pprint import pprint

location = 'berlin'

response = request_poi(location)

pprint(response)