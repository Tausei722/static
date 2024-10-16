web: gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT --static-root=static --log-file -
release: python manage.py collectstatic --noinput