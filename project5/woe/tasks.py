from celery import shared_task
from scripts import api_functions


@shared_task
def update_data():
    print("Updating data!")
    # Update the data via scripts.api_functions
    api_functions.run()
    return True
