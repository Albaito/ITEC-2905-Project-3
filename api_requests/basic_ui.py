'''
This is the "main" file for the application. It handles all user input and calls other functions throughout the application to compile and display data to the user.
'''

import datetime
from datetime import datetime
from datetime import date
from poi_output import compile_poi_data
from climate_output import compile_climate_data
from geocode_output import geocode_validation
from youtube_output import get_youtube_video
from basic_ui_menu import *
from basic_ui_db_interface import *
from prettytable import PrettyTable

# get location from user
def get_location():
    location = input('\nPlease enter your destination city or country: ')
    is_invalid = geocode_validation(location)
    while is_invalid:
        location = input('\nInvalid location. Check your spelling and try again: ')
        is_invalid = geocode_validation(location)
        if is_invalid == False:
            break
    return location

# get date from user
def get_date():
    date_string = input('\nPlease enter the date of your trip (use YYYY-MM-DD format): ')
    format_valid = date_format_validation(date_string)
    while format_valid is not True:
        date_string = input('\nInvalid format. Please enter date in YYYY-MM-DD format: ')
        format_valid = date_format_validation(date_string)
        if format_valid:
            break
    
    days_diff = date_range_validation(date_string)
    while days_diff > 365:
        date_string = input('\nPlease enter a date within the next year: ')
        days_diff = date_range_validation(date_string)
        if days_diff < 365:
            break
    return date_string

# validate the date input
def date_format_validation(date_string):
    try:
        date.fromisoformat(date_string)
        date_valid = True
    except ValueError:
        date_valid = False
    return date_valid

# dates more than one year in the future won't work with this app (by design)
# validate date range
def date_range_validation(date_string):
    today_date = str(date.today())
    today_date_formatted = datetime.strptime(today_date, '%Y-%m-%d')
    date_string_formatted = datetime.strptime(date_string, '%Y-%m-%d')
    date_diff = date_string_formatted - today_date_formatted
    days_diff = date_diff.days
    return days_diff

# get a list of climate data
def get_climate_list(location, date):
    climate_list = compile_climate_data(location, date)
    return climate_list

# get a list of poi data
def get_poi_list(location):
    poi_list = compile_poi_data(location)
    return poi_list

# get info from youtube_api
def get_youtube_info(location):
    title, id = get_youtube_video(location)
    return title, id

# build the youtube URL
def build_youtube_url(id):
    url_base = 'https://www.youtube.com/watch?v=x'
    video_url = url_base + id
    return video_url

# build a table to display climate data
def build_climate_table(climate_list):
    climate_table = PrettyTable(['Day', 'High', 'Low', 'Precip Amount', 'Precip Duration'])
    for i in climate_list:
        day_count = climate_list.index(i) + 1
        climate_table.add_row([day_count, i.high, i.low, i.precip, i.precip_time])
    return climate_table

# build a table to display poi data
def build_poi_table(poi_list):
    poi_table = PrettyTable(['Name', 'City', 'Latitude', 'Longitude'])
    for i in poi_list:
        poi_table.add_row([i.name, i.city, i.lat, i.long])
    return poi_table

# build a table to display youtube data
def build_youtube_table(title, id):
    youtube_table = PrettyTable(['Video Title', 'URL'])
    url = build_youtube_url(id)
    youtube_table.add_row([title, url])
    return youtube_table

# build a table to display a list of bookmarks
def build_bookmarks_table():
    bookmarks = view_all_bookmarks()
    bookmarks_table = PrettyTable(['ID', 'Location'])
    for i in bookmarks:
        bookmarks_table.add_row([i.id, i.location])
    print('\n')
    print(bookmarks_table)

# generate tables for the lookup output
def get_tables():
    location = get_location()
    date = get_date()
    climate_list = get_climate_list(location, date)
    poi_list = get_poi_list(location)
    video_title, video_id = get_youtube_video(location)
    climate_table = build_climate_table(climate_list)
    poi_table = build_poi_table(poi_list)
    youtube_table = build_youtube_table(video_title, video_id)
    return climate_table, poi_table, youtube_table, location, climate_list, poi_list

# generate tables for the bookmark output
def get_bookmark_tables(id):
    climate_list = get_bookmark_climate(id)
    poi_list = get_bookmark_poi(id)
    climate_table = build_climate_table(climate_list)
    poi_table = build_poi_table(poi_list)
    return climate_table, poi_table

# print lookup results tables
def print_tables():
    climate_table, poi_table, youtube_table, location, climate_list, poi_list = get_tables()
    print('\n')
    print('Here is what the weather was like a year before that date: ')
    print(climate_table)
    print('\n')
    print('Here are some nearby points of interest to check out: ')
    print(poi_table)
    print('\n')
    print('Here is a YouTube video that might be about that location: ')
    print(youtube_table)
    print('\n')
    user_add_prompt(location, climate_list, poi_list)

# print bookmark tables
def print_bookmark_tables(id):
    climate_table, poi_table = get_bookmark_tables(id)
    print('\n')
    print('Here is what the weather was like a year before that date: ')
    print(climate_table)
    print('\n')
    print('Here are some nearby points of interest to check out: ')
    print(poi_table)
    print('\n')
    get_user_selection()

# print a menu and get user input, call other functions based on input
def get_user_selection():
    print('\nTourist Research App\n')
    menu = menu_table()
    print(menu)
    selection = input('\nWhat would you like to do? Enter a number: ')
    selection_valid = user_selection_validation(selection)
    if selection_valid == 1:
        print_tables()
    elif selection_valid == 2:
        build_bookmarks_table()
        bookmark_add_input()
    elif selection_valid == 3:
        print('Thanks, bye!')
        quit()

# ask user to save bookmark and get ID
def bookmark_add_input():
    view = input('\nView a bookmark? y/n ')
    if view.upper() == 'Y':
        view_id = input('\nEnter bookmark ID: ')
        bookmark_id = int(view_id)
        print_bookmark_tables(bookmark_id)
    else:
        get_user_selection()

# validate the user menu item selection
def user_selection_validation(selection):
    selection_int = user_selection_is_int(selection)
    selection_list = [1, 2, 3]
    while selection_int not in selection_list:
        selection = input('\nInvalid selection. Try again: ')
        selection_int = user_selection_is_int(selection)
        if selection_int in selection_list:
            break
    return selection_int

# if selection can't be converted to an int, return a value outside of the valid range
def user_selection_is_int(selection):
    try:
        selection = int(selection)
        return selection
    except ValueError:
        return 4

# add bookmark to db
def add_to_db(location, cds, pois):
    bm_id = add_bookmark(location)
    add_climate_days_to_bookmark(cds, bm_id)
    add_pois_to_bookmark(pois, bm_id)

# ask if user wants to bookmark location
def user_add_prompt(location, cds, pois):
    add = input('Add location to bookmarks? y/n ')
    if add.upper() == 'Y':
        add_to_db(location, cds, pois)
        get_user_selection()
    else:
        get_user_selection()

def main():
    get_user_selection()

main()