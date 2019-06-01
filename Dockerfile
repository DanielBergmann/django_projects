FROM python:3.7
MAINTAINER Daniel Bergmann
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY . ./
COPY ./static /static
WORKDIR /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
WORKDIR /usr/src/app/coffeehouse
RUN python manage.py collectstatic --noinput
CMD exec gunicorn coffehouse.wsgi:application --bind 0.0.0.0:8000 --workers 3


