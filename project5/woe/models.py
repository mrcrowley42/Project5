from django.db import models

# Create your models here.


class Source(models.Model):
    """ Defines the Sources Table"""
    name = models.CharField(max_length=255)
    wmo_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"Source object. url:{self.url}"


class Observation(models.Model):
    """ Defines the Observations table."""
    # temp wind speed, direciton dewpoint.
    wmo = models.ForeignKey(Source, default=1, on_delete=models.SET_DEFAULT)
    # wmo = models.CharField(max_length=255, default=None, blank=True, null=True)
    local_date_time_full = models.IntegerField(default=None, blank=True, null=True)
    air_temp = models.FloatField(max_length=255, default=None, blank=True, null=True)
    dewpt = models.FloatField(max_length=255, default=None, blank=True, null=True)
    wind_dir = models.CharField(max_length=255, default=None, blank=True, null=True)
    wind_spd_kmh = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):

        return f"Observation object. Temperature:{self.air_temp}"


    # location = models.ForeignKey(Source, default=1, on_delete=models.SET_DEFAULT)
