from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([album_1, album_2, album_3, album_4, album_5, album_6, album_7, album_8, album_9, album_10, photo_album_1])

# class Media:
#     js = (
#         '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
#         '../photohandling/assets/myjs.js',       # project static folder
#     )