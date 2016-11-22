import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


json_file = './json/albums.json'


def main():
    sys.stdout.write('Loading albums.json... ')
    albums = load_json(json_file)
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating Album objects... ')
    create_Album_objects(albums)
    sys.stdout.write(Fore.GREEN + 'OK\n')


def create_Album_objects(albums):
    for album in albums:
        create_Album_object(album)


def create_Album_object(album):
    alpha2code = album.get('country', None)

    Country_object = None
    if alpha2code != None:
        try:
            Country_object = models.Country.objects.get(alpha2code=alpha2code)
        except:
            # Our Country object was not found in the database. Therefore,
            # we stop executing this function by returning control to the caller.
            return

    barcode = album.get('barcode', None)
    album_mbid = album['id']
    title = album['title']
    status = album.get('status', None)

    artist_mbid = album['artist']
    Artist_object = models.Artist.objects.get(mbid=artist_mbid)

    Album_object = models.Album.objects.create(country=Country_object,
                                               mbid=album_mbid,
                                               title=title,
                                               artist=Artist_object)

    if status != None:
        Album_object.status = status

    if barcode != None and barcode != '':
        Album_object.barcode = int(barcode)

    Album_object.save()


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
                artist_mbid = Artist_object.mbid
                limit = 15
                album_list = mbz.browse_releases(artist=artist_mbid,
                                                 release_type=["album"],
                                                 limit=limit)['release-list']
                # we need to record the mbid of the artist used to obtain these albums.
                # we do this by adding it as a key to the dict we'll save as JSON.
                for album in album_list:
                    album['artist'] = artist_mbid

                albums.extend(album_list)

            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Saving to albums to albums.json... ')
            write_json(albums, json_file)
            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')
            exit(1)

    main()
