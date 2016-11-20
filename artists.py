import os
import sys
import requests
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json


def main():
    sys.stdout.write('Loading artists.json... ')
    artists = load_json('./artists.json')
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating Artist objects... ')
    Artist_objects = create_Artist_objects(artists)
    sys.stdout.write(Fore.GREEN + 'DONE\n')


def create_Artist_objects(artists):
    Artist_objects = []

    for artist in artists:
        name = artist['name']
        Country_object = models.Country.objects.get(alpha2code=artist['country'])

        Artist_object = models.Artist.objects.create(name=name, country=Country_object)

        disambiguation = artist.get('disambiguation', None)
        if disambiguation != None:
            Artist_object.disambiguation = disambiguation

        category = artist.get('type', None)
        if category != None:
            Artist_object.category = category

        life_span = artist.get('life-span', None)

        if life_span != None:

            ended = life_span.get('ended', None)

            if ended == 'true':
                    Artist_object.ended = True
            elif ended == 'false':
                    Artist_object.ended = False
            elif ended == None:
                Artist_object.ended = None


        Artist_object.save()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    # initialize colorama
    init(autoreset=True)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'fetch':
            sys.stdout.write('Fetching artists from musicbrainz.org... ')
            mbz.set_useragent('play music app', '0.1', 'gabrielbusta@gmail.com')

            artists = []
            artists = mbz.search_artists(country='US', limit=100)['artist-list']
            artists.extend(mbz.search_artists(country='MX', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='VE', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='FR', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='JP', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='KR', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='BR', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='CN', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='GB', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='RU', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='IT', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='ES', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='NG', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='ZA', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='IN', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='CA', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='AU', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='NZ', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='NO', limit=100)['artist-list'])
            artists.extend(mbz.search_artists(country='AR', limit=100)['artist-list'])

            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to artists to artists.json... ')
            write_json(artists, './artists.json')
            sys.stdout.write(Fore.GREEN + 'DONE\n')

    main()
