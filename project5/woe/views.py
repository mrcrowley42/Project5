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
    wmo = request.GET.get('wmo')

    if wmo:
        data = Observation.objects.all().filter(wmo=wmo)

    data = serializers.serialize('json', data)
    return JsonResponse(json.loads(data), safe=False)
