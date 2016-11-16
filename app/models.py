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

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = ((MALE, 'Male'),
                      (FEMALE, 'Female'),
                      (OTHER, 'Other'))

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    bio = models.CharField(max_length=500)
    country = models.ForeignKey(Country)


class Track(models.Model):
    # TODO: ADD FILE PATH
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    # TODO: ADD Artist AND Release ForeignKey


class Label(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=50)
    founded_date = models.DateField()
    dissolved_date = models.DateField()
    dissolved = models.BooleanField(default=False)


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
