import os
import sys
import musicbrainzngs as mbz

def main():
    mbz.set_useragent("play music app", "0.1", "gabrielbusta@gmail.com")

    result = mbz.search_artists(type="group")\

    for key in result.keys():
        print(key)

    print("number of artist:" + str(len(result["artist-list"])))
    print("artist-list = ")
    uprint(result["artist-list"])
    # uprint(result)

    models.Country.objects.all()


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    import django
    django.setup()
    from app import models
    main()
