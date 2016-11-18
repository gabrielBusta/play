import musicbrainzngs as mbz
from utilities import uprint
import os


def main():
    mbz.set_useragent("play music app", "0.1", "gabrielbusta@gmail.com")

    result = mbz.search_artists(type="group")

    for key in result.keys():
        print(key)

    print("number of artist:" + str(len(result["artist-list"])))

    print("artist-list = ")

    uprint(result["artist-list"])

    for artist in result["artist-list"]:
        uprint(artist)
        print('\n')


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    import django
    django.setup()
    from app import models
    main()
