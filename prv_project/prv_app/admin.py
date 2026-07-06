from django.contrib import admin
from .models import Url_data
from .models import Movie_data
# Register your models here.
# host 계정을 통해 DB 계정 활성화 
class Url_Admin(admin.ModelAdmin):
    list_display = ('url_text', )

class Movie_Admin(admin.ModelAdmin):
    list_display = ('movie_text', )

admin.site.register(Url_data, Url_Admin)
admin.site.register(Movie_data, Movie_Admin)
