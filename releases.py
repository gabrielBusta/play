import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json


def main():
    sys.stdout.write('Loading artists.json... ')
    releases = load_json('./releases.json')
    sys.stdout.write(Fore.GREEN + 'DONE\n')


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

            Artist_objects = models.Artist.objects.all()

            releases = []
            for Artist_object in Artist_objects:
                releases.extend(mbz.search_releases(artist='Drake', limit=5)['release-list'])
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to releases to releases.json... ')
            write_json(releases, './releases.json')
            sys.stdout.write(Fore.GREEN + 'DONE\n')

    main()
