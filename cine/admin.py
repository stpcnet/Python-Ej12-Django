from django.contrib import admin

from .models import Director, Peliculas

admin.site.register(Peliculas)
admin.site.register(Director)

