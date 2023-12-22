from django.urls import path
from main import views as main_views

urlpatterns = [
    path("", main_views.home, name="home"),
    path("about/", main_views.about, name="about"),
    path("projects/", main_views.projects, name="projects")
]