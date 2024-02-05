import requests
from woe.models import Source, Observation  # Ignore this error -_-


def create_wmo_dict():
    """Returns a dictionary that translates a wmo_id number to the primary key in the sources table."""
    wmo_dict = dict()
    for source in Source.objects.all():
        wmo_dict[int(source.wmo_id)] = source
    return wmo_dict


def retrieve_urls():
    """Retrieves the URLS from the source table and returns them in a list."""
    urls = []
    for source in Source.objects.all():
        urls.append(source.url)
    return urls


def pull_data(url):
    """Function that pulls the first row of data from the BOM API for the given URL and return that row."""
    api_data = requests.get(url).json()
    data_set = [line for line in api_data['observations']['data']][0]
    return data_set


def enter_observation(observation):
    """Creates a new observation row and populates it using the passed in observation data."""
    obs = Observation()
    # !!! foreign key for wmo id not done yet
    # !!!!!!!!!!!! currently not setting wmo key and manually leaving it at 2
    # obs.wmo = wmo_dict[observation['wmo']]
    obs.wmo_id = 2
    obs.local_date_time_full = observation['local_date_time_full']
    obs.air_temp = observation['air_temp']
    obs.dewpt = observation['dewpt']
    obs.wind_dir = observation['wind_dir']
    obs.wind_spd_kmh = observation['wind_spd_kmh']
    return obs


def run():
    """The function that runs when the script is executed."""
    urls = retrieve_urls()
    last_n_entries = [obs.is_duplicate() for obs in Observation.objects.all().order_by('-id')[:len(urls)*2]]
    # wmo_dict = create_wmo_dict()

    for url in urls:
        data = pull_data(url)
        obs = enter_observation(data)
        if obs.is_duplicate() not in last_n_entries:
            obs.save()
            print("Object saved!")
        else:
            print("This entry already exists!")
