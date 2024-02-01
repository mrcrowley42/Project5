from celery import shared_task


@shared_task
def debug_task():
    print("WOE debug task working")
    return True


@shared_task
def update_data():
    print("Updating data!")
    # do some cool stuff here
    return True
