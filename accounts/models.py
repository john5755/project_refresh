from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Provider
from django.conf import settings

# Create your models here.

class User(AbstractUser):

    # user_tag = models.IntegerField()
    partner_id = models.IntegerField(null=True, blank=True) # 마지막 로그인 같이 한 파트너의 user_id
    favorite_genre = models.TextField(null=True)
    favorite_season = models.TextField(null=True)

    #Many to Many
    providers = models.ManyToManyField(Provider, related_name='users')

class History(models.Model):

    user_1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='history_1')
    user_2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='history_2')
    login_date = models.DateTimeField(auto_now_add=True)

