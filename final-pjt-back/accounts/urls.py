from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('history/<int:user_pk>/<int:partner_pk>/', views.update_history),
    path('history/reset/<int:user_pk>/<int:partner_pk>/', views.reset_history),
    path('delete/<int:user_pk>/',views.delete_user ),
]
