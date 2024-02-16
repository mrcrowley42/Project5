from hashlib import md5
import logging
from django.db import models
from logging_module import logging_script
from datetime import datetime
from django.conf import settings


class Source(models.Model):
    """ Defines the Sources Table.

    Contains the relevant information for each BOM datasource; the name of location, its wmo id and the url."""
    name = models.CharField(max_length=255)
    wmo_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Returns a string representation of object."""
        return f"Source object: [name: {self.name}, url:{self.url}, wmo_id: {self.wmo_id}]"

    def md5_hash(self) -> str:
        """Returns an MD5 hash of important fields."""
        important_fields = f"{self.wmo_id}, {self.name}, {self.url}"
        return md5(important_fields.encode()).hexdigest()

    def save(self, *args, **kwargs):
        """Override django save method to log the save event."""
        logging_script.log(f"{str(self)} added to database", logging.INFO)
        super(Source, self).save(*args, **kwargs)


class Observation(models.Model):
    """ Defines the Observations table."""
    wmo = models.ForeignKey(Source, default=1, blank=True, on_delete=models.CASCADE)
    local_date_time_full = models.IntegerField(default=None, blank=True, null=True)
    air_temp = models.FloatField(max_length=255, default=None, blank=True, null=True)
    dewpt = models.FloatField(max_length=255, default=None, blank=True, null=True)
    wind_dir = models.CharField(max_length=255, default=None, blank=True, null=True)
    wind_spd_kmh = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self) -> str:
        """Returns a string representation of object."""
        return f"Observation object: [Temperature: {self.air_temp}, Dew Point: {self.dewpt}]"

    def md5_hash(self) -> str:
        """Returns an MD5 hash of important fields."""
        important_fields = f"{self.wmo}, {self.local_date_time_full}, {self.dewpt, self.air_temp}, {self.wind_dir}"
        return md5(important_fields.encode()).hexdigest()

    def save(self, *args, **kwargs):
        """Override django save method to log the save event."""
        logging_script.log(f"{str(self)} added to database", logging.INFO)
        super(Observation, self).save(*args, **kwargs)

    def to_dictionary(self) -> dict:
        """Returns the necessary items of an Observation into a dictionary."""
        def convert_wind_dir(wind_dir):
            """Converts a wind direction to its numerical value."""
            wind_dir_list = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW',
                             'NW', 'NNW']
            if wind_dir in wind_dir_list:
                dir_index = wind_dir_list.index(wind_dir)
                return dir_index * 22.5
            return 0

        return dict(
            id=self.id,
            local_time=self.local_date_time_full,
            formatted_datetime=datetime.strptime(str(self.local_date_time_full), settings.DATETIME_FORMAT),
            air_temp=self.air_temp,
            dewpt=self.dewpt,
            wind_dir=convert_wind_dir(self.wind_dir),
            wind_speed_kmh=self.wind_spd_kmh
        )
