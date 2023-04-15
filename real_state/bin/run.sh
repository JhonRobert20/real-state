#!/bin/bash

# turn on bash's job control
set -m

# collect static files in /static_root
python manage.py collectstatic --noinput


# DB migrations
python manage.py migrate

# Run django and fast api
## For production
#gunicorn real_state.asgi:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --reload &
## For development
uvicorn real_state.asgi:app --workers 1 --reload --host 0.0.0.0 --port 8000 &
fg %1
