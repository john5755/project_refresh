from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from .models import History
from dj_rest_auth.registration.serializers import RegisterSerializer




class ProfileSerializer(serializers.ModelSerializer):

    # class MovieSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Movie
    #         fields = ('pk', 'title')

    # like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email','partner_id','favorite_genre','favorite_season','first_name','last_name')
        read_only_fields = ('pk','username','password1','password2' )



class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ('login_date',)



class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    favorite_season = serializers.CharField()
    favorite_genre = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'favorite_genre': self.validated_data.get('favorite_genre', ''),
            'favorite_season': self.validated_data.get('favorite_season', ''),
        }

