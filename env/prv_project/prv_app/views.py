from django.shortcuts import render
from django.http import HttpResponse
from . import shoppingMallCrawler
# Create your views here.

def prv_list(request):
    return render(request, 'prv_app/prv_list.html', {})

def button(request):
    shoppingMallCrawler.search_shop_review()
    return render(request, 'prv_app/button.html', {})

    