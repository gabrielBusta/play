import os
import sys
import platform
import musicbrainzngs as mbz
import json
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    recordings = []
    for json_file in os.listdir('./json/recordings'):
        recordings.extend(load_json('./json/recordings/' + json_file))

    for recording in recordings:
        create_Recording_object(recording)


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

    if len(sys.argv) == 2:
        if sys.argv[1] == 'fetch':
            sys.stdout.write('Setting up musicbrainz.org user agent... ')
            mbz.set_useragent('project', '0.0', 'bustamante.ulysses.pm@gmail.com ')
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Fetching recordings from musicbrainz.org ')

            # Album_objects = list(models.Album.objects.all())

            '''
            with open('./abby.txt', 'w') as f:
                for a in range(0, int(len(Album_objects) / 2)):
                    f.write(Album_objects[a].mbid + ',')

            with open('./gabriel.txt', 'w') as f:
                for a in range(int(len(Album_objects) / 2), len(Album_objects)):
                    f.write(Album_objects[a].mbid + ',')
            '''


            if platform.system() == 'Windows':
                sys.stdout.write(Fore.BLUE + 'using gabriel.txt\n')
                with open('./logs/gabriel.txt', 'r') as f:
                    string = f.read()
                    album_mbids = [album_mbid for album_mbid in string.split(',') if album_mbid != '']
            elif platform.system() == 'Darwin':
                sys.stdout.write(Fore.BLUE + 'Using abby.txt\'s\n')
                with open('./logs/abby.txt', 'r') as f:
                    string = f.read()
                    album_mbids = [album_mbid for album_mbid in string.split(',') if album_mbid != '']
            else:
                sys.stdout.write(Fore.RED + 'ERROR\n')
                sys.stdout.write(Fore.RED + 'Unsuported OS!\n')
                exit(1)

            with open('fetched.txt', 'a') as f:
                i = 0
                for album_mbid in album_mbids:
                    try:
                        Album_object = models.Album.objects.get(mbid=album_mbid)
                    except:
                        continue
                    limit = 15
                    recordings = mbz.browse_recordings(release=Album_object.mbid,
                                                       limit=limit)['recording-list']
                    for recording in recordings:
                        recording['album'] = album_mbid

                    Artist_object = Album_object.artist_set.all().first()

                    for recording in recordings:
                        recording['artist'] = Artist_object.mbid

                    i += 1
                    with open('./json/recordings/b-recordings-' + str(i) + '.json', mode='w', encoding='utf-8') as j:
                        json.dump(recordings, j)
                        f.write(album_mbid + ',')

            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')

    main()
