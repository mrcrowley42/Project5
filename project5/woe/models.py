from django.db import models
from hashlib import md5


class Source(models.Model):
    """ Defines the Sources Table"""
    name = models.CharField(max_length=255)
    wmo_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        """Returns a basic string representation of object."""
        return f"Source object: [url:{self.url}, name: {self.name}]"


class Observation(models.Model):
    """ Defines the Observations table."""
    wmo = models.ForeignKey(Source, default=1, on_delete=models.SET_DEFAULT)
    local_date_time_full = models.IntegerField(default=None, blank=True, null=True)
    air_temp = models.FloatField(max_length=255, default=None, blank=True, null=True)
    dewpt = models.FloatField(max_length=255, default=None, blank=True, null=True)
    wind_dir = models.CharField(max_length=255, default=None, blank=True, null=True)
    wind_spd_kmh = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        """Returns a basic string representation of object."""
        return f"Observation object: [Temperature: {self.air_temp}, Dew Point: {self.dewpt}]"

    def is_duplicate(self):
        """Returns an MD5 hash of important fields."""
        important_fields = f"{self.wmo}, {self.local_date_time_full}, {self.dewpt, self.air_temp}, {self.wind_dir}"
        return md5(important_fields.encode()).hexdigest()
