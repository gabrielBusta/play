import os
import sys
import platform
import musicbrainzngs as mbz
import json
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    sys.stdout.write('Loading recordings.json... ')
    recordings = load_json('./json/recordings.json')
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating Recording objects... ')
    for recording in recordings:
        create_Recording_object(recording)
    sys.stdout.write(Fore.GREEN + 'OK\n')


def create_Recording_object(recording):
    Artist_object = models.Artist.objects.get(mbid=recording['artist'])
    Album_object = models.Album.objects.get(mbid=recording['album'])
    mbid = recording['id']
    title = recording['title']
    length = recording.get('length', None)

    Recording_object = models.Recording.objects.create(mbid=mbid,
                                                       title=title,
                                                       album=Album_object,
                                                       artist=Artist_object)
    if length != None:
        length = int(length)
        Recording_object.length = length
    else:
        Recording_object.length = None

    Recording_object.save()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    # initialize colorama
    init(autoreset=True)

    main()
