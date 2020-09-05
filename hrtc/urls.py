from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("search", views.search, name="search"),
    path("details", views.details, name="details"),
    path("track", views.track, name="track"),
    path("slides", views.slides, name="slides"),
    path("side", views.side, name="side"),
]
