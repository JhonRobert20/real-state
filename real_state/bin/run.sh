#!/bin/bash

# turn on bash's job control
set -m

# collect static files in /static_root
python manage.py collectstatic --noinput


# DB migrations
python manage.py migrate

# Run django and fast api
gunicorn real_state.asgi:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --reload &
fg %1
