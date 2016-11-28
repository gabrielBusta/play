from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=100, default='')
    usd_rate = models.DecimalField(max_digits=15, decimal_places=10)
    iso_code = models.CharField(max_length=3)


class TimeZone(models.Model):
    utc_offset = models.CharField(max_length=9)


class Language(models.Model):
    english_name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=2)


class Country(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField('Language')
    region = models.CharField(max_length=50)
    subregion = models.CharField(max_length=70)
    population = models.PositiveIntegerField()
    timezones = models.ManyToManyField('TimeZone')
    currencies = models.ManyToManyField('Currency')
    alpha2code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.alpha2code


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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey('Artist')
    barcode = models.BigIntegerField(null=True, blank=True, default=None)
    country = models.ForeignKey('Country', null=True)
    mbid = models.CharField(max_length=36)
    title = models.CharField(max_length=300)
    status = models.CharField(max_length=50, blank=True, default='')
    date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Recording(models.Model):
    mbid = models.CharField(max_length=36)
    title = models.CharField(max_length=300)
    length = models.PositiveIntegerField(null=True, blank=True, default=None)
    artist = models.ForeignKey('Artist')
    album = models.ForeignKey('Album')
    price = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.ForeignKey('Country')

    cell = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    post_code = models.CharField(max_length=20)

    dob = models.DateField()

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICES = ((MALE, 'Male'),
                      (FEMALE, 'Female'),
                      (OTHER, 'Other'))

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='', blank=True)

    recordings = models.ManyToManyField('Recording')

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.user.username


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    recordings = models.ManyToManyField('Recording')
    profile = models.ForeignKey('Profile')

    def __str__(self):
        return self.user.title

    def __repr__(self):
        return self.user.title
