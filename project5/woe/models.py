from django.db import models


class Source(models.Model):
    """ Defines the Sources Table"""
    name = models.CharField(max_length=255)
    wmo_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"Source object. url:{self.url}"


class Observation(models.Model):
    """ Defines the Observations table."""
    wmo = models.ForeignKey(Source, default=1, on_delete=models.SET_DEFAULT)
    local_date_time_full = models.IntegerField(default=None, blank=True, null=True)
    air_temp = models.FloatField(max_length=255, default=None, blank=True, null=True)
    dewpt = models.FloatField(max_length=255, default=None, blank=True, null=True)
    wind_dir = models.CharField(max_length=255, default=None, blank=True, null=True)
    wind_spd_kmh = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f"Observation object. Temperature:{self.air_temp}"

    def is_duplicate(self):
        return f"{self.local_date_time_full}, {self.dewpt, self.air_temp}, {self.wind_dir}"
