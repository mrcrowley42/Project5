import json
import time
from datetime import datetime

import django.db.models
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.core import serializers

from .models import Source, Observation


def index(request):
    locations = [{'id': source.id, 'location': source.name} for source in Source.objects.all()]
    context = {
        'locations': locations
    }
    return render(request, 'index.html', context)


def admin(request):
    context = {}
    return render(request, 'admin.html', context)


def dev_page(request):
    if request.method == "POST":
        try:
            uploaded_file = request.FILES['document']
            print(uploaded_file.name, uploaded_file.size)
        except KeyError:
            pass
    context = {}
    return render(request, 'dev.html', context)


def user_page(request):
    locations = [{'id': source.id, 'location': source.name} for source in Source.objects.all()]
    context = {
        'locations': locations
    }
    return render(request, 'user_page.html', context)


def user_request(request):
    data = {}
    datetime_format = '%Y%m%d%H%M%S'

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
            default = datetime.strftime(datetime.now(), datetime_format)
        return obs_time if obs_time else default

    def observation_dict(obs: Observation) -> dict:
        """ Returns the necessary items of an Observation in a dictionary """
        return dict(
            id=obs.id,
            wmo=obs.wmo.id,
            local_time=obs.local_date_time_full,
            formatted_datetime=datetime.strptime(str(obs.local_date_time_full), datetime_format),
            location=obs.wmo.name,
            air_temp=obs.air_temp,
            dewpt=obs.dewpt,
            wind_dir=obs.wind_dir,
            wind_speed_kmh=obs.wind_spd_kmh
        )

    # wmo data filtered and sorted by local time (latest first)
    if len(wmo_list) > 0:
        for wmo in wmo_list:
            kwargs = dict(wmo=wmo,
                          local_date_time_full__gt=convert_time(after_time),
                          local_date_time_full__lt=convert_time(before_time, True))
            obs_objects = Observation.objects.all().filter(**kwargs).order_by('-local_date_time_full')
            wmo_data = [observation_dict(obs) for obs in obs_objects]
            if len(wmo_data) > 0:
                data[wmo] = wmo_data if not limit else wmo_data[:limit]

    return JsonResponse(data, safe=False)


def table_data(request):
    request.path = '/user'
    result = user_request(request)
    wmo = request.GET.getlist('wmo')[0]
    json_object = json.loads(result.content)

    first_obj = json_object[wmo][0]
    air_temp = first_obj['air_temp']
    location = first_obj['location']
    local_time = first_obj['local_time']
    dew_point = first_obj['dewpt']
    wind_dir = first_obj['wind_dir']
    wind_spe = first_obj['wind_speed_kmh']

    context = {'data': [['Location', location, 'Air Temperature', air_temp],
                        ['Time', local_time, 'Dew Point', dew_point],
                        ['Wind Direction', wind_dir, 'Wind Speed', wind_spe]]}
    return render(request, 'table_data.html', context)
