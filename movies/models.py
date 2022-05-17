from django.db import models

# Create your models here.

class Movie(models.Model):

    poster_path = models.TextField()
    adult = models.BooleanField()
    overview = models.TextField()