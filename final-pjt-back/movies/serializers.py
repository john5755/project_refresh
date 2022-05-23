from rest_framework import serializers
from .models import Movie, Cast, Comment, Provider, Genre, Rate
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'movie',)
        read_only_fields = ('movie', )


class CastSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Cast
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('provider_name','address','logo_path')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('genre_name',)

class MovieListSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    providers = ProviderSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Rate
        fields = ('pk', 'user', 'bgm_rate', 'movie',)
        read_only_fields = ('movie', )

   