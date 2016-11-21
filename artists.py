import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


json_file = './json/artists.json'


def main():
    sys.stdout.write('Loading artists.json... ')
    artists = load_json(json_file)
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating Artist objects... ')
    create_Artist_objects(artists)
    sys.stdout.write(Fore.GREEN + 'OK\n')


def create_Artist_objects(artists):
    for artist in artists:
        create_Artist_object(artist)


def create_Artist_object(artist):
    name = artist['name']
    artist_mbid = artist['id']
    Country_object = models.Country.objects.get(alpha2code=artist['country'])

    Artist_object = models.Artist.objects.create(name=name,
                                                 country=Country_object,
                                                 mbid=artist_mbid)

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
            artists = mbz.search_artists(country='US', limit=50)['artist-list']
            artists.extend(mbz.search_artists(country='MX', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='VE', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='FR', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='JP', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='KR', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='BR', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='CN', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='GB', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='RU', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='IT', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='ES', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='NG', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='ZA', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='IN', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='CA', limit=50)['artist-list'])
            artists.extend(mbz.search_artists(country='AR', limit=50)['artist-list'])

            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to artists to artists.json... ')
            write_json(artists, json_file)
            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')
            exit(1)

    main()
