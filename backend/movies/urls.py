from django.urls import path
from .views import *

urlpatterns = [

    path('', movie_list, name='movie_list'),

    path(
        'add/',
        add_movie,
        name='add_movie'
    ),
]