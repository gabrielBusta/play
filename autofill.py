import os
import sys
import musicbrainzngs as mbz
import requests
import codecs
import json


def main():
    # load countries
    with codecs.open('./countries.json', encoding='utf-8') as f:
        data = f.read()
        countries = json.loads(data)

    uprint(countries[0])
    print()

    # find all the timezones
    timezones = []
    for country in countries:
        for timezone in country['timezones']:
            if timezone not in timezones:
                timezones.append(timezone)
    print('timezones = ' + str(timezones))
    print()

    # for timezone in timezones:
        # models.TimeZone.objects.create(UTC_offset=timezone).save()

    # find all the languages
    languages = []
    for country in countries:
        for language in country['languages']:
            if language not in languages:
                languages.append(language)
    print('languages = ' + str(languages))
    print()

    # for language in languages:
        # new_language = models.Language.objects.create(ISO_639_1_code=language)
        # new_language.save()

    # save each country to our database
    for country in countries:
        # find the data from the json
        name = country['name']
        alpha2Code = country['alpha2Code']
        region = country['region']
        subregion = country['subregion']
        population = country['population']
        new_country_timezones = country['timezones']
        new_country_languages = country['languages']
        
        new_country= models.Country.objects.create(name=name, alpha2code=alpha2code, region=region,
         subregion=subregion, population=population)
    
        for timezone in new_country_timezones:
            new_t=models.TimeZone.objects.get(UTC_offset=timezone)
            new_country.timezones.add(new_t)
        
        for language in new_country_languages:
            new_language= models.Language.objects.get(ISO_639_1_code=language)
            new_country.languages.add(new_language)
        
            
            
        
        
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
