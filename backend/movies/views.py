from django.shortcuts import render,redirect
from .forms import MovieForm
from .models import Movie
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



def add_movie(request):

    form = MovieForm()

    if request.method == "POST":

        form = MovieForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            movie = form.save(commit=False)

            movie.user = request.user

            movie.save()

            return redirect('/')

    return render(
        request,
        'movies/add_movie.html',
        {'form':form}
    )
def movie_list(request):

    search = request.GET.get('search')

    if search:
        movies = Movie.objects.filter(
            title__icontains=search
        )
    else:
        movies = Movie.objects.all()

    return render(
        request,
        'movies/movie_list.html',
        {'movies':movies}
    )