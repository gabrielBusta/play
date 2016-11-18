import os
import sys
import requests
import codecs
import json
from utilities import uprint


def main():
    # load countries
    with codecs.open('./countries.json', encoding='utf-8') as f:
        data = f.read()
        countries = json.loads(data)

    # find all the timezones
    timezones = []
    for country in countries:
        for timezone in country['timezones']:
            if timezone not in timezones:
                timezones.append(timezone)

   # save the timezones to our database
    for timezone in timezones:
        new_timezone = models.TimeZone.objects.create(UTC_offset=timezone)
        new_timezone.save()

    # find all the languages
    languages = []
    for country in countries:
        for language in country['languages']:
            if language not in languages:
                languages.append(language)

    for language in languages:
        new_language = models.Language.objects.create(ISO_639_1_code=language)
        new_language.save()

    # save each country to our database
    for country in countries:
        name = country['name']
        alpha2Code = country['alpha2Code']
        region = country['region']
        subregion = country['subregion']
        population = country['population']
        new_country_timezones = country['timezones']
        new_country_languages = country['languages']

        new_country = models.Country.objects.create(name=name, alpha2Code=alpha2Code, region=region,
                                                    subregion=subregion, population=population)

        for timezone in new_country_timezones:
            timezone_entity = models.TimeZone.objects.get(UTC_offset=timezone)
            new_country.timezones.add(timezone_entity)

        for language in new_country_languages:
            language_entity = models.Language.objects.get(ISO_639_1_code=language)
            new_country.languages.add(language_entity)

        new_country.save()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    import django
    django.setup()
    from app import models
    main()
