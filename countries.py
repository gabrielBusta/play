import os
import sys
import requests
from colorama import init, Fore
from utilities import uprint, load_json, write_json


json_file = './json/countries.json'


def main():
    sys.stdout.write('Loading countries.json... ')
    countries = load_json(json_file)
    sys.stdout.write(Fore.GREEN + 'DONE\n')

    sys.stdout.write('Creating TimeZone and Language objects... ')
    time_zones = extract_unique_time_zones(countries)
    languages = extract_unique_languages(countries)
    create_TimeZone_objects(time_zones)
    create_Language_objects(languages)
    sys.stdout.write(Fore.GREEN + 'OK\n')

    # the Language and TimeZone objects must be present
    # in the database before we create the Country objects!
    sys.stdout.write('Creating Country objects... ')
    create_Country_objects(countries)
    sys.stdout.write(Fore.GREEN + 'OK\n')


def create_Country_objects(contries):
    for country in contries:
        create_Country_object(country)


def create_Country_object(country):
    name = country['name']
    alpha2code = country['alpha2Code']
    region = country['region']
    subregion = country['subregion']
    population = country['population']

    Country_object = models.Country.objects.create(name=name,
                                                   alpha2code=alpha2code,
                                                   region=region,
                                                   subregion=subregion,
                                                   population=population)

    for timezone in country['timezones']:
        TimeZone_object = models.TimeZone.objects.get(utc_offset=timezone)
        Country_object.timezones.add(TimeZone_object)

    for language in country['languages']:
        Language_object = models.Language.objects.get(iso_code=language.upper())
        Country_object.languages.add(Language_object)

    Country_object.save()


def create_Language_objects(languages):
    for language in languages:
        Language_object = models.Language.objects.create(iso_code=language.upper())


def create_TimeZone_objects(time_zones):
    for time_zone in time_zones:
        TimeZone_object = models.TimeZone.objects.create(utc_offset=time_zone)


def extract_unique_time_zones(countries):
    time_zones = []

    for country in countries:
        for time_zone in country['timezones']:
            if time_zone not in time_zones:
                time_zones.append(time_zone)

    return time_zones


def extract_unique_languages(countries):
    languages = []

    for country in countries:
        for language in country['languages']:
            if language not in languages:
                languages.append(language)

    return languages


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    # initialize color
    init(autoreset=True)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'fetch':
            sys.stdout.write('Fetching countries from restcountries.eu... ')
            response = requests.get('https://restcountries.eu/rest/v1/all')
            sys.stdout.write(Fore.GREEN + 'DONE\n')
            sys.stdout.write('Saving to countries to countries.json... ')
            write_json(response.json(), json_file)
            sys.stdout.write(Fore.GREEN + 'DONE\n')

    main()
