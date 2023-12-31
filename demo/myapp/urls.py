from django.urls import path
from . import views

urlpatterns = [
    # "" = empty path string means go to the root
    # views.home = go to views.py
    # name="home" = name of the url
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")
]