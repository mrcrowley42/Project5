import requests, json

TEST_URL = "https://reg.bom.gov.au/fwo/IDN60903/IDN60903.94926.json"


def pull_data(url):
    """
        Function to pull data from BOM API at the given URL and return new entries.
    """
    api_data = requests.get(url).json()
    data_set = [line for line in api_data['observations']['data']]
    return data_set


print(pull_data(TEST_URL))
