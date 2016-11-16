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
    # TODO: ADD FILE PATH
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    # TODO: ADD Artist AND Release ForeignKey


class Release(models.Model):
    label = models.ForeignKey(Label)
    # ADD Artist RELATIONSHIP
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    release_type = models.CharField(max_length=1, choices=(('ALBUM', 'EP', 'SINGLE'))
    # TODO: ADD LIST OF GENRES
    language = models.CharField(max_length=20)


class Label(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=50)
    founded_date = models.DateField()
    dissolved_date = models.DateField()
    dissolved = models.BooleanField(default=False)


class Playlist(models.Model):
    pass


class Library(models.Model):
    pass
