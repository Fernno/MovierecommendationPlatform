
from django.contrib import admin
from .models import Category, Movie, Comment, Favorite

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Favorite)