# Project5

### Follow `SETUP.md` instructions before continuing

Once cloned, run `python manage.py migrate` in the venv (cd into `project5` first) to create and insert required data into the sqlite3 database.
<br><br>
Run `python manage.py runserver` to start the WOE app.
<br><br>
`Celery` and `Celery Beat` is used to update the database every X mins with new data from the API.
<br>
In a separate terminal from the Django server, run `celery -A project5 worker -B` to start the worker and the beat together.
<br>
For more output add `-l info`, or `-l debug` to the end of the command.
<br><br>
**IMPORTANT:** For production the celery worker and beat should run separately. This can be done by running `celery -A project5 worker`, and `celery -A project5 beat` in two seperate terminals.
