from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Source, Observation

# Create your views here.


def index(request):
    context = {'observations': Observation.objects.all()}
    return render(request, 'index.html', context)
