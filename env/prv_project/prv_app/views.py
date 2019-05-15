from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prv_list(request):
    return render(request, 'prv_app/prv_list.html', {})
    