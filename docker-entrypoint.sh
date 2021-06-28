#!/bin/sh -e

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:7279
#gunicorn LGA.wsgi --bind 0.0.0.0:7279
