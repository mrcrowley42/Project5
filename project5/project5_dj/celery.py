import os

from celery import Celery
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project5_dj.settings')

app = Celery('project5_dj')

# Set namespace to use in settings.py (CELERY_X)
app.config_from_object('django.conf:settings', namespace='CELERY')


# Setup tasks
app.conf.CELERYBEAT_SCHEDULE = {
    'woe_update_data': {
        'task': 'woe.tasks.update_data',
        'schedule': timedelta(minutes=15),
    },
}
