from django.db import models


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

    # begin_date = models.DateField(default=None, blank=True, null=True)
    # end_date = models.DateField(default=None, blank=True, null=True)
    ended = models.NullBooleanField(blank=True, null=True)

    country = models.ForeignKey('Country')

'''
class Track(models.Model):
    # TODO: ADD FILE PATH
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    # TODO: ADD Artist AND Release ForeignKey


class Label(models.Model):
    name = models.CharField(max_length=50)
    label_type = models.CharField(max_length=50)
    country = models.CharField(max_length="2")
    # country = models.ForeignKey(Country)
    founded_date = models.DateField()
    dissolved_date = models.DateField()
    dissolved = models.BooleanField(default=False)
    disambiguation = models.CharField()


class Release(models.Model):
    label = models.ForeignKey(Label)
    # TODO: ADD Artist RELATIONSHIP
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    ALBUM = 'AL'
    SINGLE = 'SI'
    EXTENDED_PLAY = 'EP'

    RELEASE_TYPE_CHOICES = ((ALBUM, 'Album'),
                            (SINGLE, 'Single'),
                            (EXTENDED_PLAY, 'EP'))

    release_type = models.CharField(max_length=2, choices=RELEASE_TYPE_CHOICES)

    # TODO: ADD LIST OF GENRES
    language = models.CharField(max_length=20)


class Playlist(models.Model):
    pass


class Library(models.Model):
    pass
'''
