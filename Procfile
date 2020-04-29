release: python manage.py migrate --noinput
web: gunicorn mishos.wsgi:application --log-file -