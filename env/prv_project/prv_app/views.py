from django.shortcuts import render
from django.http import HttpResponse
from . import shoppingMallCrawler
from . import movieRebiewCrawler
from .models import Url_data
from .models import Movie_data
from . import splitSent
import os
# Create your views here.

def prv_list(request):
    return render(request, 'prv_app/prv_list.html')

def button(request):
    url = Url_data.objects.all() # 해당 URL DB에서 모든 필드에 대해 가져옴
    movie = Movie_data.objects.all() # 해당 영화명 DB에서 모든 필드에 대해 가져옴
    url_movie_get = request.POST.get('url_movie_text', None) # 입력 데이터 변수에 저장
    url_instance = Url_data() # DB 모델 변수 
    movie_instance = Movie_data() # DB 모델 변수
    url_movie_length = len(url_movie_get) # 입력 데이터를 다른 웹 페이지로 넘어갈 때 가져오는 입력값의 길이
    if url_movie_length > 20: # 만약 입력값의 길이가 20보다 크다면
        for i in url: # 상품 URL 크롤링이 시작되도록 한다. 
            if url_movie_get is i.url_text: # 해당 url이 db에 있다면 
                url_val = url_movie_get
                shoppingMallCrawler.search_shop_review(url_val) # 쇼핑몰 리뷰 크롤링 시작
                file_a = open("shoppingMall_all.txt",'r',encoding='utf-8') # 전체 텍스트 파일 데이터 읽기
                text_all = file_a.read()  
                splitSent.get_tags_all_url(text_all, 100) # 명사 추출
                file_a.close()

                file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8') # 긍정 텍스트 파일 데이터 읽기
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos_url(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8') # 부정 텍스트 파일 데이터 읽기
                try:
                    text_neg = file_n.read()
                    if os.stat("shoppingMall_neg.txt").st_size == 0: # 만약 부정 텍스트 파일 안에 데이터가 하나도 없다면
                        os.remove("C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png") # 전에 생성됐던 이미지 강제 삭제
                        file_n.close()
                    else:
                        splitSent.get_tags_neg_url(text_neg, 100)
                        file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html', {'url_movie_get': url_movie_length}) # 해당 웹페이지로 넘아갈 때 길이 데이터 같이 넘김
            elif url_movie_get is not i.url_text: # 만약 DB에 해당 URL 정보가 없다면
                url_instance.url_text = url_movie_get # DB 모델 변수에 저장된 text 필드에 입력된 URL 주소 저장
                url_instance.save() 
                url_val = url_instance.url_text
                shoppingMallCrawler.search_shop_review(url_val) # 쇼핑몰 크롤링 시작
                file_a = open("shoppingMall_all.txt",'r',encoding='utf-8') # 위 상황과 동일
                text_all = file_a.read() 
                splitSent.get_tags_all_url(text_all, 100)
                file_a.close()

                file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8') # 위 상황과 동일
                try:
                    text_pos = file_p.read()
                    splitSent.get_tags_pos_url(text_pos, 100)
                    file_p.close()
                except:
                    file_p.close()

                file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8') # 위 상황과 동일
                try:
                    text_neg = file_n.read()
                    if os.stat("shoppingMall_neg.txt").st_size == 0: # 위 상황과 동일
                        os.remove("C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png")
                        file_n.close()
                    else:
                        splitSent.get_tags_neg_url(text_neg, 100)
                        file_n.close()
                except:
                    file_n.close()
                return render(request, 'prv_app/button.html', {'url_movie_get': url_movie_length}) # 웹 페이지 이동 시 길이 데이터 불러옴.
    else: # 만약 20보다 작다면
        for j in movie: # 영화 리뷰 크롤링 시작
            if url_movie_get is j.movie_text: # 형태는 쇼핑몰과 동일
                movie_val = url_movie_get
                movieRebiewCrawler.movieStar(movie_val) # 영화 크롤링 시작
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
                movieRebiewCrawler.movieStar(movie_val) # 영화 크롤링 시작
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

def pos(request): # 상품 긍정 이미지 웹 페이지 함수
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_pos/url_pos.png") is True: # 해당 이미지가 존재한다면
        return render(request, 'prv_app/pos.html') # 해당 이미지에 맞는 페이지로 이동
    else: # 아니라면
        pass # 패스

def neg(request): # 상품 부정 이미지 웹 페이지 함수
    path = os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png") # path 변수에 해당 경로 설정
    try: # 설정한 경로에 대해 예외가 발생 할 수 있어서 try, except문으로 처리
        if path is True: # 해당 경로가 맞다면 
            return render(request, 'prv_app/neg.html') # 상품 부정 이미지 페이지로 이동
        else: # 아니라면
            return render(request, 'prv_app/error.html') # 에러 이미지 페이지로 이동
    except:
        return render(request, 'prv_app/error.html') # 예외 발생하면 바로 에러 이미지 페이지로 이동

def error(request): # 에러 이미지 웹 페이지 함수
    return render(request, 'prv_app/error.html')

def all(request): # 상품 전체 이미지 웹 페이지 함수
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_all/url_all.png") is True: # 전체 이미지가 있다면
        return render(request, 'prv_app/all.html') # 해당 이미지가 있는 웹 페이지로 이동
    else:
        pass

def all_m(request): # 영화 전체 이미지 웹 페이지 함수 
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_all/movie_all.png") is True: # 전체 이미지가 있다면
        return render(request, 'prv_app/all_movie.html') # 해당 이미지가 있는 웹 페이지로 이동
    else:
        pass

def pos_m(request): # 영화 긍정 이미지 웹 페이지 함수
    if os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_pos/movie_pos.png") is True: # 해당 이미지가 존재한다면
        return render(request, 'prv_app/p_movie.html') # 해당 이미지가 있는 웹 페이지로 이동
    else:
        pass

def neg_m(request): # 영화 부정 이미지 웹 페이지 함수
    path = os.path.exists("C:/Python_basic/env/prv_project/prv_app/static/img_neg/movie_neg.png") # path 변수에 해당 경로 설정
    try: # 설정한 경로에 대해 예외가 발생 할 수 있어서 try, except문으로 처리
        if path is True:  # 해당 경로가 맞다면 
            return render(request, 'prv_app/n_movie.html') # 영화 부정 이미지 페이지로 이동
        else:
            return render(request, 'prv_app/error.html') # 에러 이미지 페이지로 이동
    except: 
        return render(request, 'prv_app/error.html')  # 예외 발생하면 바로 에러 이미지 페이지로 이동