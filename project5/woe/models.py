from django.db import models

# Create your models here.


class Observation(models.Model):
    """ Defines the Observations table. """
    pass


class Source(models.Model):
    """ Defines the Sources Table """
    name = models.CharField(max_length=255)
    wmo_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
