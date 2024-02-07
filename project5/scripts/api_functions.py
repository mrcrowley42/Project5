import requests
import logging
from woe.models import Source, Observation  # Ignore this error -_-
from logging_module import logging_script  # And this one


def create_wmo_dict() -> dict:
    """Returns a dictionary that translates a wmo_id number to the corresponding primary key in the sources table."""
    wmo_dict = dict()
    for source in Source.objects.all():
        wmo_dict[int(source.wmo_id)] = source
    return wmo_dict


def retrieve_urls() -> list:
    """Retrieves the URLS from the source table and returns them in a list."""
    urls = []
    for source in Source.objects.all():
        urls.append(source.url)
    return urls


def pull_data(url: str) -> list:
    """Function that pulls the first row of data from the BOM API for the given URL, and returns that row."""
    api_data = requests.get(url).json()
    data_set = [line for line in api_data['observations']['data']][0]
    return data_set


def enter_observation(observation: dict, wmo_dict: dict) -> Observation:
    """Creates a new observation row and populates it using the passed in observation data.
    Assigns the appropriate foreign key using the wmo_dict."""
    obs = Observation()
    obs.wmo = wmo_dict[observation['wmo']]
    obs.local_date_time_full = observation['local_date_time_full']
    obs.air_temp = observation['air_temp']
    obs.dewpt = observation['dewpt']
    obs.wind_dir = observation['wind_dir']
    obs.wind_spd_kmh = observation['wind_spd_kmh']
    return obs


def run():
    """The function that runs when the script is executed.

    Retrieves the URLs for each source in the database, then pulls the most recent observation for each one.
    Object is then saved to database if it isn't present in the last 100 entries of the db."""
    urls = retrieve_urls()
    last_n_entries = [obs.md5_hash() for obs in Observation.objects.all().order_by('-id')[:100]]
    wmo_dict = create_wmo_dict()

    for url in urls:
        data = pull_data(url)
        obs = enter_observation(data, wmo_dict)
        if obs.md5_hash() not in last_n_entries:
            obs.save()
        else:
            logging_script.log(f"Entry {str(obs)} already exists", logging.DEBUG)
