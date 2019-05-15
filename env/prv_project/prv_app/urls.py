from django.urls import path
from prv_app import views

urlpatterns = [
    path("", views.prv_list, name = "prv_list")
]