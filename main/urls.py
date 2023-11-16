from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("links/", views.links, name="links"),
    path("contact/", views.contact, name="contact"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("projects/", views.projects, name="projects"),
]