from django.shortcuts import get_object_or_404, render, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CastSerailizer, MovieListSerializer, MovieSerializer,CommentSerializer, RateSerializer
from django.db.models import Avg, F
import requests
from .models import Movie, Genre ,Cast, Provider,Comment, Rate
from movies import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


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
    
    return Response(serializer.data)

@api_view(['POST'])
def create_rating(request, movie_pk):
    print(request.data)
    user = request.user
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    
    
    serializer = RateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        rate_average = Rate.objects.filter(movie=movie).aggregate(Avg('bgm_rate'))['bgm_rate__avg']
        movie.rate_average = rate_average
        movie.save()
        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
        
        # serializer = RateSerializer(ratings, many=True)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_comment(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        comments = movie.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = movie.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = movie.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

@api_view(['GET'])
def music_list(request):
    movies = Movie.objects.filter(genres__id=12)[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ground_list(request):
    user = request.user
    partner_id = user.partner_id
    partner = get_object_or_404(User, pk=partner_id)

    user_season = user.favorite_season
    partner_season = partner.favorite_season
    monthes = []
    if user_season == '겨울' or partner_season == '겨울':
        monthes.append('-12-')
        monthes.append('-01-')
        monthes.append('-02-')
    
    if user_season == '봄' or partner_season == '봄':
        monthes.append('-03-')
        monthes.append('-04-')
        monthes.append('-05-')

    if user_season == '여름' or partner_season == '여름':
        monthes.append('-06-')
        monthes.append('-07-')
        monthes.append('-08-')       

    if user_season == '가을' or partner_season == '가을':
        monthes.append('-09-')
        monthes.append('-10-')
        monthes.append('-11-')     

    user_genre_pk = Genre.objects.get(genre_name = user.favorite_genre).pk
    partner_genre_pk = Genre.objects.get(genre_name = partner.favorite_genre).pk

    movies = Movie.objects.exclude(genres__id=user_genre_pk).exclude(genres__id=partner_genre_pk)
    for month in monthes:
        movies = movies.exclude(release_date__contains=month)
    movies = movies.order_by(F('rate_average').desc(nulls_last=True))[:10]
    
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def character(request, character):
    character = character + ' '
    casts = Cast.objects.filter(character__contains=character)
    casts = casts.order_by(F('movie__rate_average').desc(nulls_last=True))[:10]
    serializer = CastSerailizer(casts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actorname(request, actorname):
    actorname = actorname + ' '
    casts = Cast.objects.filter(actor_name__contains=actorname)
    casts = casts.order_by(F('movie__rate_average').desc(nulls_last=True))[:10]
    serializer = CastSerailizer(casts, many=True)
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
    for page in range(6,1000):
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


def provider2(request):
    path = '/watch/providers/movie'
    params = {
        'api_key' : api_key,
        'language' : 'ko',
        'watch_region' : 'KR'
    }
    addresses = [
    'https://www.netflix.com/kr/',
    'https://www.primevideo.com/',
    'https://www.apple.com/kr/itunes/',
    'https://www.sunnxt.com/',
    'https://www.wavve.com/',
    'https://mubi.com/',
    'https://watcha.com/',
    'https://www.classixapp.com/',
    'https://serieson.naver.com/v2/movie',
    'https://guidedoc.tv/',
    'https://watchargo.com/',
    'https://eventive.org/',
    'https://www.cultpix.com/',
    'https://www.apple.com/kr/apple-tv-plus/',
    'https://www.filmbox.com/',
    'https://curiositystream.com/',
    'https://spamflix.com/',
    'https://www.docsville.com/',
    'https://www.wowpresentsplus.com/',
    'https://www.magellantv.com/',
    'https://www.broadwayhd.com/',
    'https://filmzie.com/',
    'https://www.dekkoo.com/',
    'https://www.truestory.film/',
    'https://dafilms.com/',
    'https://www.hoichoi.tv/viewplans',
    'https://www.disneyplus.com/ko-kr',
    'https://www.plex.tv/'
    ]
    response = requests.get(BASE_URL + path, params=params)
    providers = response.json()['results']
    target = get_list_or_404(Provider)
    for i in range(28):
        logo_path = providers[i]['logo_path']
        address = addresses[i] 
        
        target[i].logo_path = logo_path
        target[i].address  = address
        target[i].save()



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


def image(request):
    movies = get_list_or_404(Movie)
    params = {
        'api_key' : api_key,
        'language' : 'ko',
    }
    for movie in movies:
        movie_id = movie.movie_id
        path = f'/movie/{movie_id}/images'
        response = requests.get(BASE_URL + path, params=params)
        image_path_list = response.json()['backdrops']
        if image_path_list:
            image_path = image_path_list[0]['file_path']
            movie.image_path = image_path
        movie.save()