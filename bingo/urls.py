from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sortear/", views.sortear, name="sortear"),
    path("reiniciar/", views.reiniciar, name="reiniciar"),
]
