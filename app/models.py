from django.db import models


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
    # TODO ADD REFRENCE TO COUNTRY


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


class Country(model.Model):
    pass
