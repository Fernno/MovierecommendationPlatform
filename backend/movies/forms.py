from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):

    class Meta:
        model = Movie

        fields = [
            'title',
            'poster',
            'description',
            'release_date',
            'actors',
            'rating',
            'category',
            'trailer_link'
        ]