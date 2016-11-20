import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    sys.stdout.write('Loading releases-tiny.json... ')
    releases = load_json('./releases-tiny.json')
    sys.stdout.write(Fore.GREEN + 'DONE\n')
    for release in releases:
        pretty_print_json(release)


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    # initialize colorama
    init(autoreset=True)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'fetch':
            sys.stdout.write('Fetching releases from musicbrainz.org... ')

            mbz.set_useragent('academic database project', '0.1', 'abbyyy23@gmail.com')

            Artist_objects = models.Artist.objects.all()

            releases = []
            for Artist_object in Artist_objects:
                releases.extend(mbz.search_releases(artist=Artist_object.name, limit=5)['release-list'])
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to releases to releases.json... ')
            write_json(releases, './releases.json')
            sys.stdout.write(Fore.GREEN + 'DONE\n')

    main()
