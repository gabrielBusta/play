import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from app import models

models.Country.objects.all()
