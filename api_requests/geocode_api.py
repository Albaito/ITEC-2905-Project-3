import requests

geocode_url = 'https://geocoding-api.open-meteo.com/v1/search'

# call geocode API to get detailed location info from a simple input like "berlin"
def request_geocode(loc):
    geocode_query = {'name': loc}
    try:
        geocode_response = requests.get(geocode_url, params=geocode_query)
        geocode_response.raise_for_status()
        return geocode_response.json()
    
    except Exception as e:
        print(e)