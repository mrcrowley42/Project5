import os
import glob
import csv
from django.db import migrations
from scripts import api_functions
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Establish a relative filepath


def grab_data():
    """Returns a deduplicated list of dictionary objects representing the json data of a single observation.
    Json data is imported from the data folder."""
    filenames = glob.glob(os.path.join(BASE_DIR, '../../data/*.json'))
    return api_functions.load_json_from_file(filenames)


def populate_observations(apps, schema_editor):
    """Function to populate the Observations table with data returned by the grab_data function."""
    Source = apps.get_model("woe", "Source")
    Observation = apps.get_model("woe", "Observation")
    wmo_dict = create_wmo_dict(apps, schema_editor)
    data_collection = grab_data()

    for observation in data_collection:
        obs = Observation()
        obs.wmo = wmo_dict[observation['wmo']]
        obs.local_date_time_full = observation['local_date_time_full']
        obs.air_temp = observation['air_temp']
        obs.dewpt = observation['dewpt']
        obs.wind_dir = observation['wind_dir']
        obs.wind_spd_kmh = observation['wind_spd_kmh']
        obs.save()


def create_wmo_dict(apps, schema_editor):
    Source = apps.get_model("woe", "Source")
    wmo_dict = dict()
    for source in Source.objects.all():
        wmo_dict[int(source.wmo_id)] = source
    return wmo_dict


def populate_sources(apps, schema_editor):
    """Function to populate the sources table using values stored in sources.csv."""
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
