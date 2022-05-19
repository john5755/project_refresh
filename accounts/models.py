from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Provider

# Create your models here.

class User(AbstractUser):

    user_tag = models.IntegerField()
    partner_tag = models.IntegerField() # 마지막 로그인 같이 한 파트너의 user_tag
    favorite_genre = models.TextField()
    favorite_season = models.TextField()

    #Many to Many
    providers = models.ManyToManyField(Provider, related_name='users')