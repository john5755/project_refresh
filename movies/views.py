from django.shortcuts import get_object_or_404, render, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieListSerializer, MovieSerializer

import requests
from .models import Movie, Genre ,Cast, Provider

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    # movies = get_list_or_404(Movie)[:5]
    movies = Movie.objects.order_by('-pk')[:5]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = MovieSerializer(movie)
    print(type(serializer))
    return Response(serializer.data)



# database 관련 함수

'''
User Tag Reset 요청 시
1. (user1_tag == user_tag, user2_tag == partner_tag) | (user1_tag == partner_tag, user2_tag == user_tag)
2. login_date가 가장 오래된 것 찾기 (first_date)
3. login_date가 first_date 이후이면서 (user1_tag == partner_tag) | (user2_tag == partner_tag) 개수 count
4. 개수 보여줌
5. history에서 (user1_tag == user_tag) | (user2_tag == user_tag) 인 자료들 모두 삭제
6. user_tag 값 변경

'''
BASE_URL = 'https://api.themoviedb.org/3'
api_key = '77c1acb7ecfe2934617865f7edb08c4d'

def download(request):
    
    path = '/movie/popular'
    

    movie_ids = []
    for page in range(1,6):
        params = {
            'api_key' : api_key,
            'language' : 'ko',
            'page': page,
        }
        # 요청보내고 결과 저장하기
        response = requests.get(BASE_URL + path, params = params)
        data = response.json()
        movies = data['results']

        for movie in movies:
            movie_ids.append(movie['id'])

    for movie_id in movie_ids:
        path_detail = f'/movie/{movie_id}'
        params_detail = {
            'api_key' : api_key,
            'language' : 'ko',            
        }
        response = requests.get(BASE_URL + path_detail, params = params_detail)
        movie = response.json()
        poster_path = movie['poster_path']
        overview = movie['overview']
        movie_id = movie['id']
        original_title = movie['original_title']
        title = movie['title']
        tagline = movie['tagline']
        release_date = movie['release_date']
        runtime = movie['runtime']
        movie_now = Movie(
            movie_id = movie_id,
            poster_path = poster_path,
            overview = overview,
            original_title = original_title,
            title = title,
            tagline = tagline,
            runtime = runtime,
            release_date = release_date
        )
        movie_now.save()
        for genre in movie['genres']:
            genre_name = Genre.objects.get(genre_name=genre['name'])
            genre_name.movies.add(movie_now)
            genre_name.save()

'''
        for provider in providers:
            provider_name = Provider.objects.get(provider_name = provider['provider_name'])
            provider_name.movies.add(movie)
            provider_name.save()
'''


def cast(request):
    movies = get_list_or_404(Movie)
    BASE_URL = 'https://api.themoviedb.org/3'
    params = {
    'api_key' : '77c1acb7ecfe2934617865f7edb08c4d',
    'language' : 'ko',
    }
    for movie in movies:

        movie_id = movie.movie_id
        path = f'/movie/{movie_id}/credits'
        response = requests.get(BASE_URL + path, params = params)
        casts = response.json()['cast']
        for cast in casts:
            actor_name = cast['original_name']
            character = cast['character']
            actor = Cast(movie=movie, actor_name=actor_name, character=character)
            actor.save()

def provider(request):
    path = '/watch/providers/movie'
    params = {
        'api_key' : api_key,
        'language' : 'ko',
        'watch_region' : 'KR'
    }
    response = requests.get(BASE_URL + path, params=params)
    providers = response.json()['results']
    for provider in providers:
        provider_name = provider['provider_name']
        provider = Provider(provider_name=provider_name)
        provider.save()

def providerlink(request):
    movies = get_list_or_404(Movie)
    params = {
    'api_key' : '77c1acb7ecfe2934617865f7edb08c4d',
    }
    for movie in movies:
        movie_id = movie.movie_id
        path = f'/movie/{movie_id}/watch/providers'
        response = requests.get(BASE_URL + path, params = params)
        providers = response.json()['results'].get('KR',{}).get('flatrate',[])
        for provider in providers:
            provider_name = Provider.objects.get(provider_name = provider['provider_name'])
            provider_name.movies.add(movie)
            provider_name.save()

def genre(request):
    path = '/genre/movie/list'
    params = {
        'api_key' : api_key,
        'language' : 'ko',
    }
    response = requests.get(BASE_URL + path, params=params)
    genres = response.json()['genres']
    for genre in genres:
        genre_name = genre['name']
        genre = Genre(genre_name=genre_name)
        genre.save()