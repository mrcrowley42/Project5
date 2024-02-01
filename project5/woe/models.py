from django.db import models

# Create your models here.


class Source(models.Model):
    """ Defines the Sources Table"""
    name = models.CharField(max_length=255)
    wmo_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class Observation(models.Model):
    """ Defines the Observations table."""

    sort_order = models.IntegerField(default=None, blank=True, null=True)
    wmo = models.CharField(max_length=255, default=None, blank=True, null=True)
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    history_product = models.CharField(max_length=255, default=None, blank=True, null=True)
    local_date_time = models.DateTimeField(default=None, blank=True, null=True)
    local_date_time_full = models.IntegerField(default=None, blank=True, null=True)
    aifstime_utc = models.IntegerField(default=None, blank=True, null=True)
    lat = models.FloatField(max_length=255, default=None, blank=True, null=True)
    lon = models.FloatField(max_length=255, default=None, blank=True, null=True)
    apparent_t = models.FloatField(max_length=255,default=None, blank=True, null=True)
    cloud = models.CharField(max_length=255,default=None, blank=True, null=True)
    cloud_base_m = models.IntegerField(default=None, blank=True, null=True)
    cloud_oktas = models.IntegerField(default=None, blank=True, null=True)
    cloud_type_id = models.IntegerField(default=None, blank=True, null=True)
    cloud_type = models.CharField(max_length=255, default=None, blank=True, null=True)
    delta_t = models.FloatField(max_length=255, default=None, blank=True, null=True)
    gust_kmh = models.IntegerField(default=None, blank=True, null=True)
    gust_kt = models.IntegerField(default=None, blank=True, null=True)
    air_temp = models.FloatField(max_length=255, default=None, blank=True, null=True)
    dewpt = models.FloatField(max_length=255, default=None, blank=True, null=True)
    press = models.FloatField(max_length=255, default=None, blank=True, null=True)
    press_qnh = models.FloatField(max_length=255, default=None, blank=True, null=True)
    press_msl = models.FloatField(max_length=255, default=None, blank=True, null=True)
    press_tend = models.CharField(max_length=255, default=None, blank=True, null=True)
    rain_trace = models.FloatField(max_length=255, default=None, blank=True, null=True)
    rel_hum = models.IntegerField(default=None, blank=True, null=True)
    sea_state = models.CharField(max_length=255, default=None, blank=True, null=True)
    swell_dir_worded = models.CharField(max_length=255, default=None, blank=True, null=True)
    swell_height = models.CharField(max_length=255, default=None, blank=True, null=True)
    swell_period = models.CharField(max_length=255, default=None, blank=True, null=True)
    vis_km = models.IntegerField(default=None, blank=True, null=True)
    weather = models.CharField(max_length=255, default=None, blank=True, null=True)
    wind_dir = models.CharField(max_length=255, default=None, blank=True, null=True)
    wind_spd_kmh = models.IntegerField(default=None, blank=True, null=True)
    wind_spd_kt = models.IntegerField(default=None, blank=True, null=True)

    # location = models.ForeignKey(Source, default=1, on_delete=models.SET_DEFAULT)
