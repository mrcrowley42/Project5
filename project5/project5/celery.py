import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project5.settings')

app = Celery('project5')

# Set namespace to use in settings.py (CELERY_X)
app.config_from_object('django.conf:settings', namespace='CELERY')
