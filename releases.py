import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    sys.stdout.write('Loading releases.json... ')
    releases = load_json('./releases.json')
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

        artist = release['artist']

        Artist_object = models.Artist.objects.get(mbid=artist)

        Release_object = models.Release.objects.create(country=Country_object,
                                                       mbid=mbid,
                                                       title=title,
                                                       status=status,
                                                       release_type=models.Release.ALBUM)
        if barcode != None and barcode != '':
            Release_object.barcode = int(barcode)
            Release_object.save()

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
            mbz.set_useragent('database project', '0.1', 'bustamanteg3@gator.uhd.edu')

            sys.stdout.write('Fetching releases from musicbrainz.org... ')
            Artist_objects = models.Artist.objects.all()

            releases = []
            i = 0
            for Artist_object in Artist_objects:
                i += 1
                if i > 5:
                    break
                artist = Artist_object.mbid
                limit = 15
                release_list = mbz.browse_releases(artist=artist,
                                                    release_type=["album"],
                                                    limit=limit)['release-list']
                for release in release_list:
                    release['artist'] = artist

                releases.extend(release_list)

            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to releases to releases.json... ')
            write_json(releases, './releases.json')
            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')
            exit(1)

    main()
