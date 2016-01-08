# django-mi

When you need something up immediately and were tempted to use a microframework. Django Mi(ni) is your path to Django development.

Made for Django 1.9+.

# Install

`pip install djangomi`

# Simple app -example

```python
# app.py
from djangomi.init import *
settings.ROOT_URLCONF = "app"

def index(request):
    return HttpResponse("Hello World!")

urlpatterns = [
    url(r'^$', index),
]

app = get_wsgi_application()
if __name__ == '__main__':
    management.execute_from_command_line(sys.argv)
```

Django management commands available directly `python app.py` (equivalent to running `python manage.py`).
Develop: `python app.py runserver`

Everything should work as usual [Django](https://docs.djangoproject.com/)

# Using Gunicorn

Install `pip install gunicorn` and run `gunicorn app:app`

# Complete Django app -example

To use external apps it is convenient to initialize the Django framework from within settings.
```
# eg. celery.py
import settings
```

## settings.py
```
from djangomi.init import *
import os
from django.conf import settings

ROOT = os.path.dirname(os.path.realpath(__file__))
settings.ROOT_URLCONF = "app"
settings.TEMPLATE_DIRS = (
    os.path.join(ROOT, 'templates'),
)
settings.INSTALLED_APPS += [
'django.contrib.contenttypes',
'django.contrib.auth',
'django.contrib.admin',
'django.contrib.sessions',
]
```

## app.py
```
from __future__ import absolute_import

# settings
import settings

# views
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World!")

# urls
from django.conf.urls import patterns, url
urlpatterns = [
    url(r'^$', index),
]

# 'manage.py'
import sys
from django.core import management
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
if __name__ == '__main__':
    management.execute_from_command_line(sys.argv)
```
