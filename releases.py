import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    mbz.set_useragent('play music app', '0.1', 'gabrielbusta@gmail.com')
    artist = "5b11f4ce-a62d-471e-81fc-a69a8278c7da"
    limit = 25
    offset = 0
    releases = []
    page = 1
    print("fetching page number %d.." % page)
    result = mbz.browse_releases(artist=artist,
                                 includes=["labels"],
                                 release_type=["album"],
                                 limit=limit)
    uprint(result)
    #for recording in recordings['recording-list']:
        #pretty_print_json(recording)
    # for release in releases:
        # pretty_print_json(release)
    # write_json(releases, './releases-tiny.json')
    # sys.stdout.write('Loading releases-tiny.json... ')
    # releases = load_json('./releases-tiny.json')
    # sys.stdout.write(Fore.GREEN + 'DONE\n')

    # for release in releases:
        # for credit in release['artist-credit']:
            # uprint(credit['artist']['name'])
        # uprint(release['type'])
        # uprint(release['title'])

    # uprint(releases[0]['artist-credit'][0]['artist']['name'])
    # for release in releases:
        # uprint()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    # initialize colorama
    init(autoreset=True)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'fetch':
            sys.stdout.write('Setting up musicbrainz.org user agent... ')
            mbz.set_useragent('academic database project', '0.1', 'abbyyy23@gmail.com')
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Fetching releases from musicbrainz.org... ')
            Artist_objects = models.Artist.objects.all()
            releases = []
            for Artist_object in Artist_objects:
                releases.extend(mbz.search_releases(artist=Artist_object.name)['release-list'])
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to releases to releases.json... ')
            write_json(releases, './releases.json')
            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')

    main()
