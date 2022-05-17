from django.shortcuts import render
import requests
from .models import Movie

# Create your views here.

def download(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'


    params = {
        'api_key' : '77c1acb7ecfe2934617865f7edb08c4d',
        'language' : 'ko',
    }
    # 요청보내고 결과 저장하기
    response = requests.get(BASE_URL + path, params = params)
    data = response.json()
    movies = data['results']

    for movie in movies:
        poster_path = movie['poster_path']
        adult = movie['adult']
        overview = movie['overview']
        data = Movie(poster_path=poster_path, adult=adult, overview=overview)
        data.save()
        # id = movie['id']
        # c_path = f'/movie/{id}/credits'
        # cast = requests.get(BASE_URL + c_path, params=params)
        # c_data = cast.json()

        # for c in c_data:
        #     if c['name'] == 'harry':
