def main():
    mbz.set_useragent("play music app", "0.1", "gabrielbusta@gmail.com")

    result = mbz.search_releases(artist="Drake", release="Views", limit=1)
    print(result)

    models.Country.objects.all()


if __name__ == '__main__':
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    import django
    django.setup()
    from app import models
    import musicbrainzngs as mbz
    main()
