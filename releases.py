import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    sys.stdout.write('Loading releases.json... ')
    releases = load_json('./releases-tiny.json')
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating Release objects... ')
    for release in releases:
        alpha2code = release.get('country', None)
        if alpha2code != None:
            try:
                Country_object = models.Country.objects.get(alpha2code=alpha2code)
            except:
                continue

        barcode = release.get('barcode', None)
        mbid = release['id']
        title = release['title']
        status = release['status']

        artist = "4f8916d6-a7d2-43e9-96b6-ce3168c39c84"

        Artist_object = models.Artist.objects.get(mbid=artist)

        models.Release.objects.create(barcode=barcode,
                                      country=Country_object,
                                      mbid=mbid,
                                      title=title,
                                      status=status,
                                      release_type=models.Release.ALBUM)

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
            sys.stdout.write('Setting up musicbrainz.org user agent... ')
            '''
            mbz.set_useragent('play music app', '0.1', 'gabrielbusta@gmail.com')
            artist = "4f8916d6-a7d2-43e9-96b6-ce3168c39c84"
            limit = 25
            offset = 0
            releases = []
            page = 1
            print("fetching page number %d.." % page)
            releases = mbz.browse_releases(artist=artist,
                                           includes=[],
                                           release_type=["album"],
                                           limit=limit)

            write_json(releases['release-list'], './releases-tiny.json')
            '''
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
