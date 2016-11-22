import os
import sys
import musicbrainzngs as mbz
import json
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    pass
    # tracks = []
    # for json_file in os.listdir('./json/recordings'):
        # tracks.extend(load_json('./json/recordings/' + json_file))
    # for t in tracks:
        # pretty_print_json(tracks)



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
            mbz.set_useragent('database project', '0.1', 'gabrielbusta@gmail.com')
            sys.stdout.write(Fore.GREEN + 'DONE\n')

            sys.stdout.write('Fetching recordings from musicbrainz.org... ')
            Album_objects = models.Album.objects.all()

            with open('fetched.txt', 'a') as f:
                i = 0
                for Album_object in Album_objects:
                    album_mbid = Album_object.mbid
                    limit = 15
                    recordings = mbz.browse_recordings(release=album_mbid,
                                                       limit=limit)['recording-list']
                    for recording in recordings:
                        recording['album'] = album_mbid

                    Artist_object = Album_object.artist_set.all().first()

                    for recording in recordings:
                        recording['artist'] = Artist_object.mbid

                    i += 1
                    with open('./json/recordings/recordings' + str(i) + '.json', mode='w', encoding='utf-8') as j:
                        json.dump(recordings, j)
                        f.write(album_mbid + ',')

            sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')

    main()
