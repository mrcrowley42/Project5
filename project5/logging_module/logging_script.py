import logging
from django.conf import settings

log_level_dict = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING,
                  'critical': logging.CRITICAL}

## FILE NAME PER DAY LOGIC HERE

logging.basicConfig(filename=settings.LOGGING_OUTPUT_PATH, encoding='utf-8', level=log_level_dict[settings.DEBUG_LEVEL])


def log(message, level=logging.INFO):
    logging.log(level, message)
