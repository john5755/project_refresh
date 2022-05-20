from django.contrib import admin
from .models import Movie, Comment, Cast, Rate, Genre, Provider

# Register your models here.

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Cast)
admin.site.register(Rate)
admin.site.register(Genre)
admin.site.register(Provider)