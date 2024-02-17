from datetime import datetime
from django.conf import settings


def convert_time(obs_time, before=False):
    default = 0
    if before:
        default = datetime.strftime(datetime.now(), settings.DATETIME_FORMAT)
    return obs_time if obs_time else default


