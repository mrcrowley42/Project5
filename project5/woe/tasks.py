from celery import shared_task
from scripts.api_functions import run


@shared_task
def debug_task():
    print("WOE debug: tasks working")
    return True


@shared_task
def update_data():
    print("Updating data!")
    run()
    return True
