from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Source, Observation


def index(request):
    context = {
        'observations': Observation.objects.all(),
        'locations': ['Canberra', 'Batemans Bay']
    }
    return render(request, 'index.html', context)


def admin(request):
    context = {}
    return render(request, 'admin.html', context)


def dev_page(request):
    context = {}
    return render(request, 'dev.html', context)
