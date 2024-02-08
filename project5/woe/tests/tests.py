import json
from django.http import HttpResponse
from django.test import TestCase
from django.core import serializers
from project5.logging_module import logging_script
from woe.models import Source, Observation
from project5.scripts.api_functions import *


class ApiTests(TestCase):
    def test_api_to_db(self):
        """Test that json data is correctly recorded in database."""
        with open('woe/tests/data/dummy.json') as fh:
            data = json.load(fh)
        api_data = [line for line in data['observations']['data']][0]
        self.assertEqual(2, 2)
        wmo_dict = create_wmo_dict()
        obs = enter_observation(api_data, wmo_dict)
        obs.save()
        last_entry = Observation.objects.all().order_by('-id')[0]
        self.assertEqual(last_entry.local_date_time_full, int(api_data['local_date_time_full']))
        self.assertEqual(last_entry.air_temp, api_data['air_temp'])
        self.assertEqual(last_entry.dewpt, api_data['dewpt'])
        self.assertEqual(last_entry.wind_dir, api_data['wind_dir'])
        self.assertEqual(last_entry.wind_spd_kmh, api_data['wind_spd_kmh'])


def test_filter_wmo():
    """Test that selecting a wmo on webpage correctly results in filtered data."""
    assert 3 == 2
