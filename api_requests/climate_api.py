import requests
from datetime import datetime
from datetime import timedelta
from geocode_api import request_geocode
from pprint import pprint

climate_url = 'https://archive-api.open-meteo.com/v1/archive?'

location = 'berlin'
date_string = '2023-01-06'
daily_data = 'temperature_2m_min,temperature_2m_max,temperature_2m_mean,precipitation_sum,precipitation_hours'

# extract latitude, longitude, and timezone from the geocode JSON
def get_latitude(geo):
    lat = geo['results'][0]['latitude']
    return lat

def get_longitude(geo):
    long = geo['results'][0]['longitude']
    return long

def get_timezone(geo):
    # hardcode a timezone for UTC in the event that the JSON doesn't include a timezone (such as when a country is entered as a location)
    try:
        tz = geo['results'][0]['timezone']
    except KeyError:
        tz = 'Europe/London'
    return tz

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

# call climate API with parameters pulled from location and date input
def request_climate(loc, date_string):
    geocode = request_geocode(loc)
    lat = get_latitude(geocode)
    long = get_longitude(geocode)
    date = get_date(date_string)
    start = get_start_date(date)
    end = get_end_date(date)
    daily = daily_data
    tz = get_timezone(geocode)
    climate_query = {'latitude': lat, 'longitude': long, 'start_date': start, 'end_date': end, 'daily': daily, 'timezone': tz}
    try:
        climate_response = requests.get(climate_url, params=climate_query)
        climate_response.raise_for_status()
        return climate_response.json()
    
    except Exception as e:
        print(e)

def main():
    response = request_climate(location, date_string)

    pprint(response)

main()
