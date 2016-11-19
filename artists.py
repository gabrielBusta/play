import os
import sys
import requests
from utilities import uprint, load_json, write_json
import musicbrainzngs as mbz


def main():
    artists = []

    mbz.set_useragent('play music app', '0.1', 'gabrielbusta@gmail.com')

    artists = mbz.search_artists(country='US', limit=100)['artist-list']
    artists = mbz.search_artists(country='MX', limit=100)['artist-list']
    artists = mbz.search_artists(country='VE', limit=100)['artist-list']
    print(len(artists))
    # write_json(artists, './artists.json')
    exit(0)

    for key in result.keys():
        print(key)

    print('number of artist:' + str(len(result['artist-list'])))

    print('artist-list = ')

    uprint(result['artist-list'])

    for artist in result['artist-list']:
        uprint(artist)
        print('\n')


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models
    main()
