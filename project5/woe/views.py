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
    context = {}
    return render(request, 'dev.html', context)


def user_request(request):
    data = {}
    wmo_list: list = request.GET.getlist('wmo')
    before_time = request.GET.get('before')
    after_time = request.GET.get('after')
    limit = request.GET.get('limit', 0)
    try:
        limit = max(0, int(limit))
    except ValueError as e:
        raise ValueError(f"Parameter 'limit' ({limit}) is not a valid number.\n{e}")

    def get_datetime_from_data(string):
        try:
            return datetime.strptime(str(string), '%Y%m%d%H%M%S')
        except ValueError:
            return 0

    def observation_dict(obs: Observation) -> dict:
        """ Returns the necessary items of an Observation in a dictionary """
        return dict(
            id=obs.id,
            wmo=obs.wmo.id,
            local_time=obs.local_date_time_full,
            formatted_datetime=get_datetime_from_data(obs.local_date_time_full),
            location=obs.wmo.name,
            air_temp=obs.air_temp,
            dewpt=obs.dewpt,
            wind_dir=obs.wind_dir,
            wind_speed_kmh=obs.wind_spd_kmh
        )

    # wmo data
    if len(wmo_list) > 0:
        for wmo in wmo_list:
            kwargs = dict(wmo=wmo)
            wmo_data = [observation_dict(obs) for obs in Observation.objects.all().filter(**kwargs)]
            if len(wmo_data) > 0:
                data[wmo] = wmo_data if not limit else wmo_data[:limit]

    return JsonResponse(data, safe=False)


def table_data(request):
    request.path = '/user'
    result = user_request(request)
    wmo = request.GET.getlist('wmo')[0]
    json_object = json.loads(result.content)
    air_temp = json_object[wmo][0]['air_temp']
    location = json_object[wmo][0]['location']
    time = json_object[wmo][0]['local_time']
    dew_point = json_object[wmo][0]['dewpt']
    wind_dir = json_object[wmo][0]['wind_dir']
    wind_spe = json_object[wmo][0]['wind_speed_kmh']
    context = {'data': [['Location', location, 'Air Temperature', air_temp],
                        ['Time', time, 'Dew Point', dew_point],
                        ['Wind Direction', wind_dir, 'Wind Speed', wind_spe]]}
    return render(request, 'table_data.html', context)

