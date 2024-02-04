from django.contrib import admin
from .models import Observation, Source
# Register your models here.
admin.site.register(Observation, Source)
