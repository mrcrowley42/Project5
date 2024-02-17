from helpers.api_functions import load_json_from_memory, create_wmo_dict, enter_observation


def upload_json(request):
    """Takes files uploaded by the user and saves the compatible json to database."""
    wmo_dict = create_wmo_dict()
    try:
        json_files = [file for file in request.FILES.getlist('document') if file.content_type == "application/json"]
        for json_file in json_files:
            file_contents = json_file.file.read()
            observations = load_json_from_memory(file_contents)
            for observation in observations:
                obs = enter_observation(observation, wmo_dict)
                obs.save()
    # IMPROVE THIS
    except Exception as error:
        print(type(error).__name__, error.args)
        pass
