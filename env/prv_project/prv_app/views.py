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
    url_movie_get = request.POST.get('url_movie_text', None)
    url_instance = Url_data()
    movie_instance = Movie_data()
    url_movie_length = len(url_movie_get)
    if url_movie_length > 20:
        for i in url:
            if url_movie_get is i.url_text:
                url_val = url_movie_get
                shoppingMallCrawler.search_shop_review(url_val)
                file_a = open("shoppingMall_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all_url(text_all, 100)
                file_a.close()

                file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos_url(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    if os.stat("shoppingMall_neg.txt").st_size == 0:
                        os.remove("C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png")
                        file_n.close()
                    else:
                        splitSent.get_tags_neg_url(text_neg, 100)
                        file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html', {'url_movie_get': url_movie_length})
            elif url_movie_get is not i.url_text:
                url_instance.url_text = url_movie_get
                url_instance.save()
                url_val = url_instance.url_text
                shoppingMallCrawler.search_shop_review(url_val)
                file_a = open("shoppingMall_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all_url(text_all, 100)
                file_a.close()

                file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos_url(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    if os.stat("shoppingMall_neg.txt").st_size == 0:
                        os.remove("C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png")
                        file_n.close()
                    else:
                        splitSent.get_tags_neg_url(text_neg, 100)
                        file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html', {'url_movie_get': url_movie_length})
    else:
        for j in movie:
            if url_movie_get is j.movie_text:
                movie_val = url_movie_get
                movieRebiewCrawler.movie_craw(movie_val)
                file_a = open("movie_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all_movie(text_all, 100)
                file_a.close()

                file_p = open("movie_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos_movie(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("movie_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    if os.stat("movie_neg.txt").st_size == 0:
                        os.remove("C:/Python_basic/env/prv_project/prv_app/static/img_neg/movie_neg.png")
                        file_n.close()
                    else:
                        splitSent.get_tags_neg_movie(text_neg, 100)
                        file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html', {'url_movie_get': url_movie_length})
            elif url_movie_get is not j.movie_text:
                movie_instance.movie_text = url_movie_get
                movie_instance.save()
                movie_val = movie_instance.movie_text
                movieRebiewCrawler.movie_craw(movie_val)
                file_a = open("movie_all.txt",'r',encoding='utf-8')
                text_all = file_a.read() 
                splitSent.get_tags_all_movie(text_all, 100)
                file_a.close()

                file_p = open("movie_pos.txt",'r',encoding='utf-8')
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos_movie(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("movie_neg.txt",'r',encoding='utf-8')
                try:
                    text_neg = file_n.read()
                    if os.stat("movie_neg.txt").st_size == 0:
                        os.remove("C:/Python_basic/env/prv_project/prv_app/static/img_neg/movie_neg.png")
                        file_n.close()
                    else:
                        splitSent.get_tags_neg_movie(text_neg, 100)
                        file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html', {'url_movie_get': url_movie_length})

def pos(request):
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_pos/url_pos.png") is True:
        return render(request, 'prv_app/pos.html')
    else:
        pass

def neg(request):
    path = os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png")
    try:
        if path is True:
            return render(request, 'prv_app/neg.html')
        else:
            return render(request, 'prv_app/error.html')
    except:
        return render(request, 'prv_app/error.html')

def error(request):
    return render(request, 'prv_app/error.html')

def all(request):
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_all/url_all.png") is True:
        return render(request, 'prv_app/all.html')
    else:
        pass

def all_m(request):
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_all/movie_all.png") is True:
        return render(request, 'prv_app/all_movie.html')
    else:
        pass

def pos_m(request):
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_pos/movie_pos.png") is True:
        return render(request, 'prv_app/p_movie.html')
    else:
        pass

def neg_m(request):
    path = os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_neg/movie_neg.png")
    try:
        if path is True:
            return render(request, 'prv_app/n_movie.html')
        else:
            return render(request, 'prv_app/error.html')
    except:
        return render(request, 'prv_app/error.html')