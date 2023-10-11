import requests
import os
from pprint import pprint

climate_url = 'https://archive-api.open-meteo.com/v1/archive?'

latitude = '44.96'
longitude = '-93.2638'
start_date = '2023-09-18'
end_date = '2023-10-02'
daily_data = 'temperature_2m_min,temperature_2m_max,temperature_2m_mean,precipitation_sum,precipitation_hours'
timezone = 'America/Chicago'

def request_climate(lat, long, start, end, daily, tz):
    climate_query = {'latitude': lat, 'longitude': long, 'start_date': start, 'end_date': end, 'daily': daily, 'timezone': tz}
    try:
        climate_response = requests.get(climate_url, params=climate_query)
        climate_response.raise_for_status()
        return climate_response.json()
    
    except Exception as e:
        print(e)

def main():
    response = request_climate(latitude, longitude, start_date, end_date, daily_data, timezone)
    pprint(response)

main()
