from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)
    primary_language = models.CharField(max_length=20)
    country_code = models.CharField(max_length=3)

class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    begin_date = models.DateField()
    end_date = models.DateField()
    ended = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=(
             ('M', 'F'),
             ('m', 'f')))
    bio = models.CharField(max_length=500)
    country = models.ForeignKey(Country)


class Track(models.Model):
    pass


class Release(models.Model):
    pass


class Label(models.Model):
    pass


class Playlist(models.Model):
    pass


class Library(models.Model):
    pass
