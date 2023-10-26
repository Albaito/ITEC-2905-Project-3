'''
This file contains unit tests for climate_output.py
'''

import unittest
from unittest import TestCase
from unittest.mock import patch

from climate_api import *
from climate_output import *
from class_defs import ClimateDay

mock_climate_response = {'latitude': 55.800003, 'longitude': 37.600006, 'generationtime_ms': 0.07009506225585938, 'utc_offset_seconds': 10800, 'timezone': 'Europe/Moscow', 'timezone_abbreviation': 'MSK', 'elevation': 141.0, 'daily_units': {'time': 'iso8601', 'temperature_2m_min': '°C', 'temperature_2m_max': '°C', 'temperature_2m_mean': '°C', 'precipitation_sum': 'mm', 'precipitation_hours': 'h'}, 'daily': {'time': ['2023-10-08', '2023-10-09', '2023-10-10', '2023-10-11', '2023-10-12', '2023-10-13', '2023-10-14'], 'temperature_2m_min': [1.8, 1.8, 1.2, -2.4, 6.1, 5.3, 5.0], 'temperature_2m_max': [6.7, 5.3, 4.8, 6.6, 12.8, 11.5, 13.8], 'temperature_2m_mean': [4.1, 3.4, 2.4, 2.9, 9.6, 8.7, 9.3], 'precipitation_sum': [7.1, 3.3, 1.5, 0.0, 2.2, 0.0, 4.4], 'precipitation_hours': [24.0, 17.0, 9.0, 0.0, 14.0, 0.0, 10.0]}}

class TestClimateOutput(TestCase):

    @patch('climate_output.request_climate')
    def test_compile_climate_data(self, mock_api):
        mock_api.return_value = mock_climate_response

        location = 'Moscow'
        date = '2024-10-10'
        count = 0
        expected_days = []
        expected_high = [6.7, 5.3, 4.8, 6.6, 12.8, 11.5, 13.8]
        expected_low = [1.8, 1.8, 1.2, -2.4, 6.1, 5.3, 5.0]
        expected_precip = [7.1, 3.3, 1.5, 0.0, 2.2, 0.0, 4.4]
        expected_precip_time = [24.0, 17.0, 9.0, 0.0, 14.0, 0.0, 10.0]

        while count < len(expected_high):
            day = ClimateDay(expected_high[count], expected_low[count], expected_precip[count], expected_precip_time[count])
            expected_days.append(day)
            count = count + 1

        days = compile_climate_data(location, date)

        self.assertEqual(expected_days, days)

if __name__ == '__main__':
    unittest.main()