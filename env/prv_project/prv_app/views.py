from django.shortcuts import render
from django.http import HttpResponse
from . import shoppingMallCrawler
from . import movieRebiewCrawler
from .models import Url_data
from .models import Movie_data
# Create your views here.

def prv_list(request):
    return render(request, 'prv_app/prv_list.html')

def button(request):
    url = Url_data.objects.all()
    movie = Movie_data.objects.all()
    url_get = request.POST.get('url_movie_text', None)
    movie_get = request.POST.get('url_movie_text', None)
    url_instance = Url_data()
    movie_instance = Movie_data()
    for i in url:
        if url_get in i.url_text:
            url_val = url_get
            shoppingMallCrawler.search_shop_review(url_val)
            return render(request, 'prv_app/button.html')
        elif url_get not in i.url_text:
            url_instance.url_text = url_get
            url_instance.save()
            url_val = url_get
            shoppingMallCrawler.search_shop_review(url_val)
            return render(request, 'prv_app/button.html')
    for j in movie:
        if movie_get in j.movie_text:
            movie_val = movie_get
            movieRebiewCrawler.movie_craw(movie_val)
            return render(request, 'prv_app/button.html')
        elif movie_get not in j.movie_text:
            movie_instance.movie_text = movie_get
            movie_instance.save()
            movie_val = movie_get
            movieRebiewCrawler.movie_craw(movie_val)
            return render(request, 'prv_app/button.html')