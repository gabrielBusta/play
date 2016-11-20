import os
import sys
import musicbrainzngs as mbz
from colorama import init, Fore
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    pass

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

            sys.stdout.write('Fetching tracks from musicbrainz.org... ')
            uprint(mbz.search_recordings(album='Album'))

            sys.stdout.write(Fore.GREEN + 'DONE\n')

            # sys.stdout.write('Saving to releases to releases.json... ')
            # write_json(releases, './releases.json')
            # sys.stdout.write(Fore.GREEN + 'DONE\n')
        else:
            sys.stdout.write(Fore.RED + 'ERROR\n')
            sys.stdout.write(Fore.RED + 'Invalid argument!\n')

    main()
