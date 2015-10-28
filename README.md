# django-mi

When you need something up immediately and were tempted to use a microframework. Django Mi(ni) is your path to Django development.

Made for Django 1.9.

# Install

`pip install djangomi`

# Usage

```bash
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
