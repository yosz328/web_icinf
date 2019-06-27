#! /bin/bash

# apply database migration
echo "Applying migrations"
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# collect static
echo "Collecting static files"
python manage.py collectstatic --no-input

# start server
echo "Starting server"
python manage.py runserver 0:8080