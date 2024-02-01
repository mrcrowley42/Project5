from django.db import migrations
import os, json, glob, csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Establish a relative filepath


def grab_data():
    """Returns a deduplicated list of dictionary objects representing the json data of a single observation.
    Json data is imported from the data folder."""
    
    files = glob.glob(os.path.join(BASE_DIR, '../../data/*.json'))
    data_collection = []
    for file in files:
        with open(file) as fh:
            data = json.load(fh)
            data_collection.append([line for line in data['observations']['data']])

    deduplicated_data = []
    for dataset in data_collection:
        for observation in dataset:
            observation.pop('sort_order')
            if observation not in deduplicated_data:
                deduplicated_data.append(observation)

    return deduplicated_data


def populate_observations(apps, schema_editor):
    """Function to populate the Observations table with data returned by the grab_data function."""

    Source = apps.get_model("woe", "Source")
    Observation = apps.get_model("woe", "Observation")

    data_collection = grab_data()

    for observation in data_collection:
        obs = Observation()

        # obs.wmo = Source(observation['wmo'])
        obs.wmo = observation['wmo']
        obs.local_date_time_full = observation['local_date_time_full']
        obs.air_temp = observation['air_temp']
        obs.dewpt = observation['dewpt']
        obs.wind_dir = observation['wind_dir']
        obs.wind_spd_kmh = observation['wind_spd_kmh']
        obs.save()

    # for value in [2, 6, 3, 5]:
    #     obs = Observation()
    #     obs.wmo = Source(value)
    #     obs.name = "canberra"
    #     obs.save()


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
