import requests, json
from django.db import migrations

# from .models import Observation, Source

# export DJANGO_SETTINGS_MODULE=project5.settings

TEST_URL = "https://reg.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"

def create_wmo_dict():

    wmo_dict = dict()
    for source in Source.objects.all():
        wmo_dict[source.wmo_id] = source.id
    return wmo_dict


def retrieve_urls():
    pass

    # return urls


def pull_data(url):
    """
        Function to pull data from BOM API at the given URL and return new entries.
    """
    api_data = requests.get(url).json()
    data_set = [line for line in api_data['observations']['data']][0]
    return data_set


def enter_observation(observation):
    # NEEDS to check if data is already in database first

    obs = Observation()
    # obs.wmo = wmo_dict[observation['wmo']]
    obs.local_date_time_full = observation['local_date_time_full']
    obs.air_temp = observation['air_temp']
    obs.dewpt = observation['dewpt']
    obs.wind_dir = observation['wind_dir']
    obs.wind_spd_kmh = observation['wind_spd_kmh']
    obs.save()


# print(create_wmo_dict(apps, schema_editor))
print(pull_data(TEST_URL))
