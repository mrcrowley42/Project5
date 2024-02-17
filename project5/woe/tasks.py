from celery import shared_task
from helpers import api_functions


@shared_task
def update_data_task():
    print("Updating data!")
    # Update the data via api_functions.update_data
    api_functions.update_data()
    return True


@shared_task
def upload_json_task():
    print("Uploading and Processing files!")

    return True
