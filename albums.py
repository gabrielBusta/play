import os
import sys
import datetime
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

    date = album.get('date', None)
    if date != None:
        if date.count('-') == 2:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        elif date.count('-') == 1:
            date = datetime.datetime.strptime(date, "%Y-%m").date()
        elif date.count('-') == 0:
            date = datetime.datetime.strptime(date, "%Y").date()

    Album_object.date = date

    Album_object.save()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    # initialize colorama
    init(autoreset=True)

    main()
