from __future__ import absolute_import
import os, sys
from django.conf import settings
from django.conf.global_settings import *

SECRET_KEY = os.getenv('SECRET_KEY', 'not_so_secret')
DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'

if not settings.configured:
    settings.configure(**locals())

# minimal imports
import json
from django.http import HttpResponse
from django.conf.urls import patterns, url
from django.core import management
from django.core.wsgi import get_wsgi_application
