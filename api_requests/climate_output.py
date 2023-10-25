from climate_api import request_climate
from class_defs import ClimateDay

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

def compile_climate_data(location, date):
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