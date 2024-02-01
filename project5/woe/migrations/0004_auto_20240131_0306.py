# Generated by Django 4.2.9 on 2024-01-31 03:06
import csv
from django.db import migrations
import os, json, glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Establish a relative filepath


def grab_data():
    """Returns a list of datasets for each json file located in the data folder.
       Each dataset contains a list of dictionary objects that represent the json data for a single observation."""
    files = glob.glob(os.path.join(BASE_DIR, '../../data/*.json'))
    data_collection = []
    for file in files:
        with open(file) as fh:
            data = json.load(fh)
            data_collection.append([line for line in data['observations']['data']])
    return data_collection


def populate_observations(apps, schema_editor):
    """
        Function to populate the Observations table with data from json files.
    """

    Source = apps.get_model("woe", "Source")
    Observation = apps.get_model("woe", "Observation")

    data_collection = grab_data()
    for dataset in data_collection:
        for observation in dataset:
            obs = Observation()
            obs.sort_order = observation['sort_order']
            obs.wmo = observation['wmo']
            obs.name = observation['name']
            obs.history_product = observation['history_product']
            # obs.local_date_time = observation['local_date_time']
            obs.local_date_time_full = observation['local_date_time_full']
            obs.aifstime_utc = observation['aifstime_utc']
            obs.lat = observation['lat']
            obs.lon = observation['lon']
            obs.apparent_t = observation['apparent_t']
            obs.cloud = observation['cloud']
            obs.cloud_base_m = observation['cloud_base_m']
            obs.cloud_oktas = observation['cloud_oktas']
            obs.cloud_type_id = observation['cloud_type_id']
            obs.cloud_type = observation['cloud_type']
            obs.delta_t = observation['delta_t']
            obs.gust_kmh = observation['gust_kmh']
            obs.gust_kt = observation['gust_kt']
            obs.air_temp = observation['air_temp']
            obs.dewpt = observation['dewpt']
            obs.press = observation['press']
            obs.press_qnh = observation['press_qnh']
            obs.press_msl = observation['press_msl']
            obs.press_tend = observation['press_tend']
            obs.rain_trace = observation['rain_trace']
            obs.rel_hum = observation['rel_hum']
            obs.sea_state = observation['sea_state']
            obs.swell_dir_worded = observation['swell_dir_worded']
            obs.swell_height = observation['swell_height']
            obs.swell_period = observation['swell_period']
            # obs.vis_km = observation['vis_km']
            obs.weather = observation['weather']
            obs.wind_dir = observation['wind_dir']
            obs.wind_spd_kmh = observation['wind_spd_kmh']
            obs.wind_spd_kt = observation['wind_spd_kt']
            obs.save()

    # for value in [2, 6, 3, 5]:
    #     obs = Observation()
    #     obs.wmo = Source(value)
    #     obs.name = "canberra"
    #     obs.save()
        

def populate_sources(apps, schema_editor):
    """
        Function to populate the sources table using values stored in sources.csv
    """
    Source = apps.get_model("woe", "Source")
    with open(os.path.join(BASE_DIR, '../../data/Source.csv')) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            source = Source()
            source.name = line[0]
            source.wmo_id = line[1]
            source.url = line[2]
            source.save()


class Migration(migrations.Migration):

    dependencies = [
        ('woe', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_sources),
        migrations.RunPython(populate_observations)
    ]
