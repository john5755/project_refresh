from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):

    movie_id = models.IntegerField(primary_key=True)
    poster_path = models.TextField()
    original_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    tagline = models.TextField()
    overview = models.TextField()
    release_date = models.TextField()
    runtime = models.IntegerField()
    rate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rate_movies', through='Rate')
    rate_average = models.FloatField(null=True)
    image_path = models.TextField(null=True)

class Rate(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    bgm_rate = models.IntegerField()

class Genre(models.Model):

    genre_name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='genres')

class Cast(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')
    actor_name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)

class Provider(models.Model):

    provider_name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='providers')
    address = models.CharField(max_length=100, null=True, blank=True)
    logo_path = models.CharField(max_length=100, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


'''
영화 DATABASE에 안 들어가면 추가 해야 할 영화들

To All The Boys I've Loved Before.
Falling Inn Love.
Always Be My Maybe.
Irreplaceable You.
The Lovebirds.
About Time.
Alex Strangelove.
When We First Met.


'''