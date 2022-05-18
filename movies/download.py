import requests
from .models import Movie, MovieGenre

def download():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    api_key = '77c1acb7ecfe2934617865f7edb08c4d'

    movie_ids = []
    for page in range(1,3):
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
        vote_average = movie['vote_average']
        release_date = movie['release_date']
        runtime = movie['runtime']
        for genre in movie['genres']:
            genre_name = genre['name']
            MovieGenre(movie_id=movie_id, genre_name=genre_name)
            MovieGenre.save()
        Movie(
            movie_id = movie_id,
            poster_path = poster_path,
            overview = overview,
            original_title = original_title,
            title = title,
            tagline = tagline,
            vote_average= vote_average,
            runtime = runtime,
            release_date = release_date
        )
        Movie.save()