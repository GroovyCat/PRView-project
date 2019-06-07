from django.forms import ModelForm
from .models import Frl_movie
class Inputform(ModelForm):
    class Meta:
        model = Frl_movie
        fields = ['url_movie_text']