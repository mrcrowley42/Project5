import json

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
    wmo_list: list = request.GET.getlist('wmo', [])
    limit = request.GET.get('limit', 0)
    try:
        limit = int(limit)
    except ValueError as e:
        raise ValueError(f"Parameter 'limit' ({limit}) is not of type: int.\n{e}")

    def observation_dict(obs: Observation) -> dict:
        """ Returns the necessary items of an Observation in a dictionary """
        return dict(
            id=obs.id,
            wmo=obs.wmo.id,
            local_time=obs.local_date_time_full,
            air_temp=obs.air_temp,
            dewpt=obs.dewpt,
            wind_dir=obs.wind_dir,
            wind_speed_kmh=obs.wind_spd_kmh
        )

    # wmo data
    if len(wmo_list) > 0:
        for wmo in wmo_list:
            wmo_data = [observation_dict(obs) for obs in Observation.objects.all().filter(wmo=wmo)]
            if len(wmo_data) > 0:
                data[wmo] = wmo_data if not limit else wmo_data[:limit]

    return JsonResponse(data, safe=False)
