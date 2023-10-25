import datetime
from datetime import datetime
from datetime import date
from poi_output import compile_poi_data
from climate_output import compile_climate_data
from geocode_output import geocode_validation
from prettytable import PrettyTable

def get_location():
    location = input('Please enter your destination city or country: ')
    is_invalid = geocode_validation(location)
    while is_invalid:
        location = input('Invalid location. Check your spelling and try again: ')
        is_invalid = geocode_validation(location)
        if is_invalid == False:
            break
    return location

def get_date():
    date_string = input('Please enter the date of your trip (use YYYY-MM-DD format): ')
    format_valid = date_format_validation(date_string)
    while format_valid is not True:
        date_string = input('Invalid format. Please enter date in YYYY-MM-DD format: ')
        format_valid = date_format_validation(date_string)
        if format_valid:
            break
    
    days_diff = date_range_validation(date_string)
    while days_diff > 365:
        date_string = input('Please enter a date within the next year: ')
        days_diff = date_range_validation(date_string)
        if days_diff < 365:
            break
    return date_string

def date_format_validation(date_string):
    try:
        date.fromisoformat(date_string)
        date_valid = True
    except ValueError:
        date_valid = False
    return date_valid

def date_range_validation(date_string):
    today_date = str(date.today())
    today_date_formatted = datetime.strptime(today_date, '%Y-%m-%d')
    date_string_formatted = datetime.strptime(date_string, '%Y-%m-%d')
    date_diff = date_string_formatted - today_date_formatted
    days_diff = date_diff.days
    return days_diff

def get_climate_list(location, date):
    climate_list = compile_climate_data(location, date)
    return climate_list

def get_poi_list(location):
    poi_list = compile_poi_data(location)
    return poi_list

def build_climate_table(climate_list):
    climate_table = PrettyTable(['Day', 'High', 'Low', 'Precip Amount', 'Precip Duration'])
    for i in climate_list:
        day_count = climate_list.index(i) + 1
        climate_table.add_row([day_count, i.high, i.low, i.precip, i.precip_time])
    return climate_table

def build_poi_table(poi_list):
    poi_table = PrettyTable(['Name', 'City', 'Latitude', 'Longitude'])
    for i in poi_list:
        poi_table.add_row([i.name, i.city, i.lat, i.long])
    return poi_table

def get_tables():
    location = get_location()
    date = get_date()
    climate_list = get_climate_list(location, date)
    poi_list = get_poi_list(location)
    climate_table = build_climate_table(climate_list)
    poi_table = build_poi_table(poi_list)
    return climate_table, poi_table

def print_tables():
    climate_table, poi_table = get_tables()
    print('\n')
    print('Here is what the weather was like a year before that date: ')
    print(climate_table)
    print('\n')
    print('Here are some nearby points of interest to check out: ')
    print(poi_table)

def main():
    print_tables()

main()