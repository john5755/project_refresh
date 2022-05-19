from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('download/', views.download),
    path('cast/', views.cast),
    path('provider/', views.provider),
    path('providerlink/', views.providerlink),
]