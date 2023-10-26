'''
This file contains unit tests to test the basic_ui functions.
'''

import unittest
from unittest import TestCase
from unittest.mock import patch

from basic_ui import *

class TestBasicUI(TestCase):

    # @patch('builtins.input', side_effect=['3', '400', '2', '46346', '999', '0', '-1', '-200', 'Berlin'])
    # def test_get_location_int_input(self, mock_input):
    #     location = get_location()
    #     self.assertEqual('Berlin', location)

    # @patch('builtins.input', side_effect = ['2.0', '3.14', '20.0000', '25', 'Berlin'])
    # def test_get_location_float_input(self, mock_input):
    #     location = get_location()
    #     self.assertEqual('Berlin', location)

    # @patch('builtins.input', side_effect = ['2024-10-40', '2025', '2025-10-10', '2023-30-10', 'june 8th', '2024-10-10'])
    # def test_get_date_incorrect_input(self, mock_input):
    #     date = get_date()
    #     self.assertEqual('2024-10-10', date)

    def test_date_format_validation(self):
        date = '2023-13-10'
        expected_result = False
        actual_result = date_format_validation(date)
        self.assertEqual(expected_result, actual_result)

    def test_date_range_validation(self):
        date = '2100-01-01'
        expected_result = False
        actual_result = date_range_validation(date)
        self.assertEqual(expected_result, actual_result)

    def test_build_youtube_url(self):
        id = '123fakeID'
        expected_result = 'https://www.youtube.com/watch?v=123fakeID'
        actual_result = build_youtube_url(id)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()