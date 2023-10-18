from climate_api import request_climate
from pprint import pprint
from class_defs import ClimateDay

# location_string = 'berlin'
# date_string = '2020-01-10'

# def get_response(location, date):
#     response = request_climate(location, date)
#     return response

def get_precip_time_list(response):
    precip_time_list = response['daily']['precipitation_hours']
    return precip_time_list

def get_precip_list(response):
    precip_list = response['daily']['precipitation_sum']
    return precip_list

def get_high_list(response):
    high_list = response['daily']['temperature_2m_max']
    return high_list

def get_low_list(response):
    low_list = response['daily']['temperature_2m_min']
    return low_list

def compile_data(location, date):
    response = request_climate(location, date)
    day = 0
    days = []
    high = get_high_list(response)
    low = get_low_list(response)
    precip = get_precip_list(response)
    precip_time = get_precip_time_list(response)
    while day < len(high):
        day_object = ClimateDay(high[day], low[day], precip[day], precip_time[day])
        days.append(day_object)
        day = day + 1
    return days

# def main():
#     api_response = get_response(location_string, date_string)
#     day_dict = compile_data(api_response)
#     day_count = 0
#     while day_count < len(day_dict):
#         print('The high temp will be ' + str(day_dict['day' + str(day_count)].high))
#         print('The low temp will be ' + str(day_dict['day' + str(day_count)].low))
#         print('The precipitation amount will be ' + str(day_dict['day' + str(day_count)].precip))
#         print('The preciptiation duration will be ' + str(day_dict['day' + str(day_count)].precip_time))
#         day_count = day_count + 1

# main()