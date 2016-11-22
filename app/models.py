from django.db import models
from django.contrib.auth.models import User


class TimeZone(models.Model):
    utc_offset = models.CharField(max_length=9)


class Language(models.Model):
    iso_code = models.CharField(max_length=2)


class Country(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField('Language')
    region = models.CharField(max_length=50)
    subregion = models.CharField(max_length=70)
    population = models.PositiveIntegerField()
    timezones = models.ManyToManyField('TimeZone')
    alpha2code = models.CharField(max_length=2)


class Artist(models.Model):
    mbid = models.CharField(max_length=36)
    name = models.CharField(max_length=100)

    PERSON = 'Person'
    GROUP = 'Group'
    ORCHESTRA = 'Orchestra'
    CHOIR = 'Choir'
    CHARACTER = 'Character'
    OTHER = 'Other'
    NONE = ''

    CATEGORY_CHOICES = ((PERSON, 'Individual person'),
                        (GROUP, 'Band or group of people'),
                        (ORCHESTRA, 'Orchestra or large instrumental ensemble'),
                        (CHOIR, 'Choir or large vocal ensemble'),
                        (CHARACTER, 'Fictional character'),
                        (OTHER, 'Other'),
                        (NONE, 'None'))

    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='', blank=True)
    disambiguation = models.CharField(max_length=100, default='', blank=True)

    ended = models.NullBooleanField(blank=True, null=True)

    country = models.ForeignKey('Country')


class Album(models.Model):
    artist = models.ForeignKey('Artist')
    barcode = models.BigIntegerField(null=True, blank=True, default=None)
    country = models.ForeignKey('Country', null=True)
    mbid = models.CharField(max_length=36)
    title = models.CharField(max_length=300)
    status = models.CharField(max_length=50, blank=True, default='')


class Recording(models.Model):
    mbid = models.CharField(max_length=36)
    title = models.CharField(max_length=300)
    length = models.IntegerField(null=True, blank=True, default=None)
    artist = models.ForeignKey('Artist')
    album = models.ForeignKey('Album')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.ForeignKey('Country')

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'Other'

    GENDER_CHOICES = ((MALE, 'Male'),
                      (FEMALE, 'Female'),
                      (OTHER, 'Other'))

    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default='', blank=True)

    recordings = models.ManyToManyField('Recording')


class Playlist(models.Model):
    recordings = models.ManyToManyField('Recording')
    library = models.ForeignKey('Profile')
