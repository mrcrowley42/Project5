import logging
from django.conf import settings
from datetime import date
from pathlib import Path


output_path = settings.LOGGING_OUTPUT_PATH
Path(output_path).mkdir(parents=True, exist_ok=True)
log_level_dict = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING,
                  'critical': logging.CRITICAL}

LOG_FILENAME = output_path + "woe_log_" + str(date.today()) + '.log'
logging.basicConfig(filename=LOG_FILENAME, encoding='utf-8', level=log_level_dict[settings.DEBUG_LEVEL])


def log(message: str, level=logging.INFO):
    """override of the logging library's log function.
    Logs to the location specified in settings.py."""
    logging.log(level, message)
