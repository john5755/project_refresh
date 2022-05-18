from platform import release
from django.db import models

# Create your models here.

class Movie(models.Model):

    movie_id = models.IntegerField(primary_key=True)
    poster_path = models.TextField()
    original_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    tagline = models.TextField()
    vote_average = models.FloatField()
    overview = models.TextField()
    release_date = models.TextField()
    runtime = models.IntegerField()

class MovieGenre(models.Model):

    movie_id = models.IntegerField()
    genre_name = models.CharField(max_length=20)



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