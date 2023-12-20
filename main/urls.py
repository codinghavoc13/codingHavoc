from django.urls import path
from main import views as main_views
from gndn import views as gndn_views

urlpatterns = [
    path("", main_views.home, name="home"),
    path("about/", main_views.about, name="about"),
    path("projects/", main_views.projects, name="projects"),
    #gndn
    path("gndn/", gndn_views.gndn_main, name="gndn_main"),
    path("gndn/register/", gndn_views.gndn_register, name="gndn_register"),
    path("gndn/login/", gndn_views.gndn_login, name="gndn_login"),
    path("gndn/logged_in/", gndn_views.gndn_logged_in, name="gndn_logged_in"),
    path("gndn/logout/", gndn_views.logout, name="gndn_logout")
]