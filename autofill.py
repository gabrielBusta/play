import os
import sys
import musicbrainzngs as mbz
import requests

def main():
    # get every country in the world (250)
    response = requests.get('https://restcountries.eu/rest/v1/all')
    countries = response.json()
    print("countries is a " + str(type(countries)))
    print("an element of country is a " + str(type(countries[0])))
    print("there are " + str(len(countries)) + " contries")
    print()
    uprint(countries)
    # save each country to our country database
    # for country in countries:
        # find the data from the json
        # name =
        # region =
        # subregion =
        # population =
        # timezones =
        # languages =
        # models.Country.objects.create(name=name, region=region, subregion=subregion,
        #                               population=population, languages=languages)

    # mbz.set_useragent("play music app", "0.1", "gabrielbusta@gmail.com")

    # result = mbz.search_artists(type="group")

    # for key in result.keys():
        # print(key)

    # print("number of artist:" + str(len(result["artist-list"])))

    # print("artist-list = ")

    # uprint(result["artist-list"])

    # for artist in result["artist-list"]:
        # print()
        # uprint(artist)
        # print()

    # uprint(result)


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
