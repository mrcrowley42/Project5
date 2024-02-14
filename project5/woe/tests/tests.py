import json
from django.http import HttpResponse, HttpResponsePermanentRedirect
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


class UserRequestTests(TestCase):
    """ Tests the user request endpoint is working as expected """
    def get_expected(self):
        with open('woe/tests/data/user_request_data.json', 'r') as fh:
            return json.load(fh)

    def test_basic_user_request(self):
        """ Test response received from `wmo = 2` """
        response = self.client.get('/user', {'wmo': 3}).json()

        self.assertEqual(self.get_expected(), response)

    def test_limited_user_request(self):
        """ Test response received from `wmo = 2` and `limit = 3` """
        response = self.client.get('/user', {'wmo': 3, 'limit': 3}).json()
        expected = self.get_expected()
        expected[0]['observations'] = expected[0]['observations'][:3]  # remove last object
        self.assertEqual(expected, response)

    def test_time_restricted_user_request(self):
        """ Test response received from `wmo = 2` and `before = 20240201090000` and `after = 20240129090000`

        Essentially getting everything before the first `wmo=2` object and after the last `wmo=2` object """
        response = self.client.get('/user', {'wmo': 3, 'before': 20240204210000, 'after': 20240128130000}).json()
        expected = self.get_expected()
        observations = expected[0]['observations']
        expected[0]['observations'] = observations[1:len(observations) - 1]  # remove first and last object
        self.assertEqual(expected, response)


class DBTests(TestCase):
    """ Tests various features that interact with the database """
    def test_edit_source(self):
        new_name = 'newname'
        source = Source.objects.get(id=1)
        self.client.post('/admin/', {'id': source.id, 'name': new_name, 'wmo_id': source.wmo_id, 'url': source.url})
        self.assertEqual(Source.objects.get(id=1).name, new_name)

    def test_delete_entry(self):
        self.assertEqual(1, 2)
