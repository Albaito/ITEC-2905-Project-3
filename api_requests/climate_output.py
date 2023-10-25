from climate_api import request_climate
from pprint import pprint

location = 'berlin'
date = '2020-01-10'

response = request_climate(location, date)

pprint(response)