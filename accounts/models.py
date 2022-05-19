from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Provider
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):

    # user_tag = models.IntegerField()
    partner_id = models.IntegerField() # 마지막 로그인 같이 한 파트너의 user_id
    favorite_genre = models.TextField()
    favorite_season = models.TextField()

    #Many to Many
    providers = models.ManyToManyField(Provider, related_name='users')

class History(models.Model):

    user_1 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='history_1')
    user_2 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='history_2')
    login_date = models.DateTimeField(auto_now_add=True)