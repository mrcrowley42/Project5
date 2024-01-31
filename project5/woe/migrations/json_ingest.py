import os, json, glob


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Establish a relative filepath


class Observation():
    def __init__(self):
        pass


def grab_data():
    files = glob.glob(os.path.join(BASE_DIR, '../../data/*.json'))
    data_collection = []
    for file in files:
        with open(file) as fh:
            data = json.load(fh)
            data_collection.append([line for line in data['observations']['data']])
    return data_collection


def create_observation(data):
    obs = Observation()
    obs.location = data['wmo']
    return obs


def ingest_json():
    data = grab_data()
    for dataset in data:
        for observation in dataset:
            gg = create_observation(observation)
            print(gg.location)

            # print(observation)

    # with open(os.path.join(BASE_DIR, '../../data/IDN60903.94926.json')) as file:
    #     data = json.load(file)
    #     for line in data['observations']['data']:
    #         print(line["history_product"])

        # for line in reader:
        #     source = Source()
        #     source.name = line[0]
        #     source.wmo_id = line[1]
        #     source.url = line[2]
        #     source.save()


ingest_json()
