NetMon README
=============

## Steps to install
First, clone the repository.

    git clone https://github.com/thomai/netmon.git

Satisfy some dependencies (you should prefer a virtual environment).

* Django 1.8
* pytz
* djangorestframework
* django-braces

Next, create the django sqlite3 database.

    python manage.py migrate

Finally, create a django superuser.

    python manage.py createsuperuser

Now you're ready to start the django server.

    manage.py runserver 0.0.0.0:8080

## Backup/Restore
Execute the following command to back up your data ...

    python manage.py dumpdata --indent 2 --output netmon_backup.json

... and the following to restore your data ...

    python manage.py loaddata netmon_backup.json
