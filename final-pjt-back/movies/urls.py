from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # download data
    path('genre/', views.genre),
    path('download/', views.download),
    path('cast/', views.cast),
    path('provider/', views.provider),
    path('provider2/', views.provider2),
    path('providerlink/', views.providerlink),

    #movie
    path('movielist/', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),

    #comment
    path('<int:movie_pk>/comments/', views.create_comment),
    path('<int:moive_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),

    #rating
    path('<int:movie_pk>/rating/', views.create_rating ),

    #bgm
    path('musiclist/', views.music_list, name='music_list'),
    path('groundlist/', views.ground_list, name='ground_list'),
]