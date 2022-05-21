from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from .models import History

class ProfileSerializer(serializers.ModelSerializer):

    # class MovieSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Movie
    #         fields = ('pk', 'title')

    # like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email',)

class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ('login_date',)

