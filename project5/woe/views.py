import json
from datetime import datetime, date
from django.http import JsonResponse
from django.shortcuts import render, redirect
from scripts import api_functions
from scripts.api_functions import load_json_from_memory, create_wmo_dict, enter_observation
from .models import Source, Observation
from django.forms.models import model_to_dict
from django.conf import settings



def index(request):
    """View for the home page."""
    context = {}
    return render(request, 'index.html', context)


def admin(request):
    """View for the admin page."""
    wmo_dict = create_wmo_dict()
    serialized_dict = {}
    for key, object in wmo_dict.items():
        serialized_dict[key] = model_to_dict(object)
    context = {'data': Source.objects.all(), 'wmo_dict': json.dumps(serialized_dict)}
    if request.method == "POST":
        post_data = request.POST.dict()
        print(post_data)
        source = Source()
        source.name = post_data['name']

        source.url = post_data['url']
        print(post_data['wmo_id'].isnumeric())

        source.wmo_id = int(post_data['wmo_id']) if post_data['wmo_id'].isnumeric() else 0
        if post_data['id']:
            source.id = int(post_data['id'])
        print(source)
        source.save()
        return redirect('admin')

    return render(request, 'admin.html', context={'data': context})


def dev_page(request):
    """View for the developer page."""
    context = {}
    if request.method == "POST":
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

    return render(request, 'dev.html', context)


def user_page(request):
    """View for the user page."""
    locations = [{'id': source.id, 'location': source.name} for source in Source.objects.all()]
    context = {
        'locations': locations
    }
    return render(request, 'user_page.html', context)


def user_request(request):
    """
    Request for data from the server

    Data format: [{wmo_id: x, location: y, observations: [{...}, {...}]}, ...]

    Parameters:

    - wmo = location ID (supports multiple)
    - before = before datetime (format: YYYYMMDDhhmmss)
    - after = after datetime (format: YYYYMMDDhhmmss)
    - limit = limit results by amount (must be a number)
    """
    data = []

    wmo_list: list = request.GET.getlist('wmo')
    before_time = request.GET.get('before')
    after_time = request.GET.get('after')
    limit = request.GET.get('limit', 0)
    try:
        limit = max(0, int(limit))
    except ValueError as e:
        raise ValueError(f"Parameter 'limit' ({limit}) is not a valid number.\n{e}")

    def convert_time(obs_time, before=False):
        default = 0
        if before:
            default = datetime.strftime(datetime.now(), settings.DATETIME_FORMAT)
        return obs_time if obs_time else default

    if len(wmo_list) > 0:
        for wmo in wmo_list:
            kwargs = dict(wmo=wmo,
                          local_date_time_full__gt=convert_time(after_time),
                          local_date_time_full__lt=convert_time(before_time, True))
            observations = Observation.objects.all().filter(**kwargs).order_by('-local_date_time_full')
            wmo_data = [obs.to_dictionary() for obs in observations]
            if len(wmo_data) > 0:
                data.append(dict(
                    wmo_id=wmo,
                    location=Source.objects.get(id=wmo).name,
                    observations=wmo_data if not limit else wmo_data[:limit]
                ))

    return JsonResponse(data, safe=False)


def user_request_chart(request):
    """
    Request for formatted chart data (data format same as user request)

    Parameters:

    - All the same as user request
    - type = the type of data (multiple supported, e.g. air_temp, dewpt)
    """
    data_type_list = request.GET.getlist('type')
    wmo_list = request.GET.getlist('wmo')

    request.path = '/user'
    data = json.loads(user_request(request).content)

    for i, wmo in enumerate(wmo_list):
        observations = data[i]['observations']
        data[i]['observations'] = []
        for observation in observations:
            data_types = {data_type: observation[data_type] for data_type in data_type_list}
            data_types['local_time'] = observation['local_time']
            data_types['formatted_datetime'] = observation['formatted_datetime']
            data[i]['observations'].append(data_types)
    return JsonResponse(data, safe=False)


def table_data(request):
    """Returns html table content."""
    request.path = '/user'
    result = user_request(request)

    if len(json.loads(result.content)):
        first_wmo = json.loads(result.content)[0]
        first_obs = first_wmo['observations'][0]

        air_temp = first_obs['air_temp']
        location = first_wmo['location']
        local_time = first_obs['local_time']
        dew_point = first_obs['dewpt']
        wind_dir = first_obs['wind_dir']
        wind_spe = first_obs['wind_speed_kmh']

        context = {'data': [['Location', location, 'Air Temperature', air_temp],
                            ['Time', local_time, 'Dew Point', dew_point],
                            ['Wind Direction', wind_dir, 'Wind Speed', wind_spe]]}
        return render(request, 'table_data.html', context)
    else:
        context = {}
        return render(request, 'table_data.html', context)


def do_manual_ingest(request):
    """Calls api_functions' run method to manually ingest data."""
    api_functions.run()
    return redirect('admin')


def remove_from_source_table(request):
    """Removes a source entry from the sources table. """
    post_data = int(request.POST['id'])
    try:
        Source.objects.get(pk=post_data).delete()
    except KeyError:
        pass

    return redirect('admin')


def load_log(request):
    """Returns the current days' log contents."""
    filepath = settings.LOGGING_OUTPUT_PATH + "woe_log_" + str(date.today()) + '.log'
    with open(filepath) as fp:
        log_data = fp.read()

    return JsonResponse(log_data, safe=False)
