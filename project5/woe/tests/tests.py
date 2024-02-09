import json
from django.http import HttpResponse
from django.test import TestCase
from django.core import serializers
from project5.logging_module import logging_script
from woe.models import Source, Observation
from project5.scripts.api_functions import *


class ApiTests(TestCase):
    """Tests related to API functionality."""
    def test_api_to_db(self):
        """Test that json data is correctly recorded in database."""
        data = json.load(open('woe/tests/data/dummy.json'))
        api_data = [line for line in data['observations']['data']][0]
        wmo_dict = create_wmo_dict()
        obs = enter_observation(api_data, wmo_dict)
        obs.save()
        last_entry = Observation.objects.all().order_by('-id')[0]

        self.assertEqual(last_entry.local_date_time_full, int(api_data['local_date_time_full']))
        self.assertEqual(last_entry.air_temp, api_data['air_temp'])
        self.assertEqual(last_entry.dewpt, api_data['dewpt'])
        self.assertEqual(last_entry.wind_dir, api_data['wind_dir'])
        self.assertEqual(last_entry.wind_spd_kmh, api_data['wind_spd_kmh'])

    def test_duplicates(self):
        """Test that duplicate entries when loading json from file are ignored."""
        filenames = ['woe/tests/data/duplicates.json',]  # Expected number of entries is 2.
        wmo_dict = create_wmo_dict()
        data_collection = load_json_from_file(filenames)
        start_value = len(Observation.objects.all())
        for observation in data_collection:
            obs = Observation()
            obs.wmo = wmo_dict[observation['wmo']]
            obs.local_date_time_full = observation['local_date_time_full']
            obs.air_temp = observation['air_temp']
            obs.dewpt = observation['dewpt']
            obs.wind_dir = observation['wind_dir']
            obs.wind_spd_kmh = observation['wind_spd_kmh']
            obs.save()
        last_entries = Observation.objects.all().order_by('-id')[:2]
        end_value = len(Observation.objects.all())
        self.assertEqual(end_value, start_value + 2)
        self.assertNotEquals(last_entries[0], last_entries[1])



