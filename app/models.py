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


class Track(models.Model):
    name = models.CharField(max_length=50)
    disamgibuaition = models.CharField(max_length=50)
    length = models.IntegerField()
    #duration = models.DurationField()
    # TODO: ADD Artist AND Release ForeignKey
    artist = models.ForeignKey('Artist')
    release = models.ForeignKey('Release')


class Release(models.Model):
    # TODO: ADD Artist RELATIONSHIP
    country = models.ForeignKey('Country')
    name = models.CharField(max_length=50)
    disambiguation = models.CharField(max_length=100)

    ALBUM = 'Album'
    SINGLE = 'Single'
    EXTENDED_PLAY = 'EP'
    BROADCAST = 'Broadcast'
    OTHER= 'Other'

    RELEASE_TYPE_CHOICES = ((ALBUM, 'Album'),
                            (SINGLE, 'Single'),
                            (EXTENDED_PLAY, 'EP'),
                            (BROADCAST, 'Broadcast'))

    release_type = models.CharField(max_length=20, choices=RELEASE_TYPE_CHOICES)


class Playlist(models.Model):
    pass


class Library(models.Model):
    pass
