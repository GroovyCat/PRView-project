from django.shortcuts import render
from django.http import HttpResponse
from . import shoppingMallCrawler
from . import movieRebiewCrawler
from .models import Url_data
from .models import Movie_data
from . import splitSent
import os
from . import splitSent
from . import Pos_KR_WC
from . import Depos_KR_WC
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
    url_length = len(url_get)
    movie_length = len(movie_get)
    if url_length > movie_length:
        for i in url:
            if url_get is i.url_text:
                url_val = url_get
                shoppingMallCrawler.search_shop_review(url_val)
                file_a = open("shoppingMall_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all(text_all, 100)
                file_a.close()

                file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    splitSent.get_tags_neg(text_neg, 100)
                    file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html')
            elif url_get is not i.url_text:
                url_instance.url_text = url_get
                url_instance.save()
                url_val = url_instance.url_text
                shoppingMallCrawler.search_shop_review(url_val)
                file_a = open("shoppingMall_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all(text_all, 100)
                file_a.close()

                file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    splitSent.get_tags_neg(text_neg, 100)
                    file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html')
    else:
        for j in movie:
            if movie_get is j.movie_text:
                movie_val = movie_get
                movieRebiewCrawler.movie_craw(movie_val)
                file_a = open("movie_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all(text_all, 100)
                file_a.close()

                file_p = open("movie_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("movie_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    splitSent.get_tags_neg(text_neg, 100)
                    file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html')
            elif movie_get is not j.movie_text:
                movie_instance.movie_text = movie_get
                movie_instance.save()
                movie_val = movie_instance.movie_text
                movieRebiewCrawler.movie_craw(movie_val)
                file_a = open("movie_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all(text_all, 100)
                file_a.close()

                file_p = open("movie_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("movie_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    splitSent.get_tags_neg(text_neg, 100)
                    file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html')

def pos(request):
    return render(request, 'prv_app/pos.html')
     

def neg(request):
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_url_neg/url_neg.png") is False:
        return render(request, 'prv_app/error.html')
    else:
        return render(request, 'prv_app/neg.html')

def error(request):
    return render(request, 'prv_app/error.html')