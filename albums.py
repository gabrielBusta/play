import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    sys.stdout.write('Loading albums.json... ')
    albums = load_json('./albums.json')
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating Album objects... ')
    for album in albums:
        alpha2code = album.get('country', None)
        if alpha2code != None:
            try:
                Country_object = models.Country.objects.get(alpha2code=alpha2code)
            except:
                continue

        barcode = album.get('barcode', None)
        mbid = album['id']
        title = album['title']
        status = album.get('status', None)

        artist = album['artist']

        Artist_object = models.Artist.objects.get(mbid=artist)

        Album_object = models.Album.objects.create(country=Country_object,
                                                   mbid=mbid,
                                                   title=title)

        if status != None:
            Album_object.status = status

        if barcode != None and barcode != '':
            Album_object.barcode = int(barcode)

        Album_object.save()

        Artist_object.albums.add(Album_object)

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
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Fetching albums from musicbrainz.org... ')
            Artist_objects = models.Artist.objects.all()

            albums = []
            for Artist_object in Artist_objects:
                artist = Artist_object.mbid
                limit = 15
                album_list = mbz.browse_releases(artist=artist,
                                                 release_type=["album"],
                                                 limit=limit)['release-list']
                for album in album_list:
                    album['artist'] = artist

                albums.extend(album_list)

            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to albums to albums.json... ')
            write_json(albums, './albums.json')
            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')
            exit(1)

    main()
