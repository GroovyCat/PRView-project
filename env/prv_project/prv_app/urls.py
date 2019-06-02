from django.urls import path
from prv_app import views
app_name = "prv_app"
urlpatterns = [
    path("", views.prv_list, name = "prv_list"),
    path("button", views.button, name = "button")
]