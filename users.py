import os
from colorama import init, Fore
import random
import datetime
import requests
from utilities import uprint, load_json, write_json, pretty_print_json


def main():
    Album_objects = Album.objects.all()
    users = load_json('./json/users.json')
    lorem = load_json('./json/lorem.json')
    for user in users:
        create_user_profile(user, Album_objects, lorem)


def create_user_profile(user, Album_objects, lorem):
    username = user['login']['username']
    first_name = user['name']['first']
    last_name = user['name']['last']
    email = user['email']
    password = user['login']['password']

    User_object = User.objects.create(username=username,
                                      first_name=first_name,
                                      last_name=last_name,
                                      email=email,
                                      password=password)

    country = user['nat']
    Country_object = Country.objects.get(alpha2code=country)

    cell = user['cell']
    phone = user['phone']
    gender = user['gender']
    street = user['location']['street']
    city = user['location']['city']
    state = user['location']['state']
    post_code = user['location']['postcode']

    dob = user['dob'].split()
    dob = datetime.datetime.strptime(dob[0], "%Y-%m-%d").date()
    profile = Profile.objects.create(user=User_object,
                                     country=Country_object,
                                     cell=cell,
                                     phone=phone,
                                     gender=gender,
                                     street=street,
                                     city=city,
                                     state=state,
                                     post_code=post_code,
                                     dob=dob)

    num_albums = random.randint(5, 20)
    used_albums_mbids = []

    for i in range(0, num_albums):
        Album_object = random.choice(Album_objects)

        while Album_object.mbid in used_albums_mbids:
             Album_object = random.choice(Album_objects)

        Recording_objects = Recording.objects.filter(album=Album_object)

        for Recording_object in Recording_objects:
            profile.recordings.add(Recording_object)

        used_albums_mbids.append(Album_object.mbid)

    num_playlist = random.randint(1, 15)
    used_titles = []
    Recording_objects = profile.recordings.all()

    for i in range(0, num_playlist):
        elem = random.choice(lorem)
        title = elem['title']
        while title in used_titles:
            title = random.choice(lorem)

        Playlist_object = Playlist.objects.create(title=title,
                                                  profile=profile)
        used_titles.append(title)

        num_records = random.randint(5, 30)
        for j in range(0, num_records):
            Recording_object = random.choice(Recording_objects)
            Playlist_object.recordings.add(Recording_object)

        Playlist_object.save()

    profile.save()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app.models import Profile, Country, Recording, Album, Playlist
    from django.contrib.auth.models import User
    # initialize colorama
    init(autoreset=True)

    main()
