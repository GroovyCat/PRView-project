from django.urls import path
from . import views
# 각 해당 웹페이지에 대한 path 설정
app_name = "prv_app"
urlpatterns = [
    path("", views.prv_list, name = "prv_list"),
    path("button/", views.button, name = "button"),
    path("url_pos/", views.pos, name="pos"),
    path("url_neg/", views.neg, name="neg"),
    path("imageError/", views.error, name="error"),
    path("url_all/", views.all, name="all"),
    path("mov_all/", views.all_m, name="all_m"),
    path("mov_pos/", views.pos_m, name="pos_m"),
    path("mov_neg/", views.neg_m, name="neg_m"),
]