import logging
from django.conf import settings
from datetime import date

log_level_dict = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING,
                  'critical': logging.CRITICAL}

LOG_FILENAME = settings.LOGGING_OUTPUT_PATH + "_" + str(date.today()) + '.log'
logging.basicConfig(filename=LOG_FILENAME, encoding='utf-8', level=log_level_dict[settings.DEBUG_LEVEL])


def log(message, level=logging.INFO):
    logging.log(level, message)
