from django.contrib import admin
from .models import Artist, Album, Recording, Profile

admin.site.site_header = 'Play Administration'

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Recording)
admin.site.register(Profile)
