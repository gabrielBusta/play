# To generate the DB
```bash
python manage.py migrate --fake app zero
```
DELETE MIGRATIONS AND pycache IN ./app/migrations
DELETE THE DATABASE
CREATE THE DATABASE
```bash
python manage.py makemigrations app
```
```bash
python manage.py migrate
```
```bash
python countries.py <fetch>
```
# Common Django Commands
## run the server at 127.0.0.1:8000
```bash
manage.py runserver
```
## stop server
| windows       | OSX    |
|:-------------:|:------:|
| `Ctrl-c`      | `⌘-c` |
## start an interactive Django shell
```bash
python manage.py shell
```
## create a superuser / administrator:
```bash
python manage.py createsuperuser
```
## update the database to match the models
```bash
python manage.py makemigrations [appname]
```
this will generate the SQL necessary to alter the database.
```bash
python manage.py migrate
```
this will **actually change the database schema** by running the SQL generated by the makemigrations command.
## create an app within the current directory:
```bash
django-admin startapp [appname]
```
**don't forget to add the app to INSTALLED_APPS in settings.py**
