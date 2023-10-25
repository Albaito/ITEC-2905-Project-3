'''
This file calls Meteo's Historical Weather API to get historical weather data. It goes back one year and returns a week's worth of weather data, 
including temperature, precipitation amount and precipitation duration.
'''

import requests
from datetime import datetime
from datetime import timedelta
from geocode_output import compile_geocode_data

climate_url = 'https://archive-api.open-meteo.com/v1/archive?'

daily_data = 'temperature_2m_min,temperature_2m_max,temperature_2m_mean,precipitation_sum,precipitation_hours'

# convert date string to date object
def get_date(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
    return date_object

# calculate start and end date
def get_start_date(date):
    start_date = date - (timedelta(days = 368))
    return start_date

def get_end_date(date):
    end_date = date - (timedelta(days = 362))
    return end_date

# call climate API with parameters pulled from geocode API response and user input
def request_climate(loc, date_string):
    lat, long, tz = compile_geocode_data(loc)
    date = get_date(date_string)
    start = get_start_date(date)
    end = get_end_date(date)
    daily = daily_data
    climate_query = {'latitude': lat, 'longitude': long, 'start_date': start, 'end_date': end, 'daily': daily, 'timezone': tz}
    try:
        climate_response = requests.get(climate_url, params=climate_query)
        climate_response.raise_for_status()
        return climate_response.json()
    
    except Exception as e:
        print(e)