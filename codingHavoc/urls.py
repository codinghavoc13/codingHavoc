"""
URL configuration for codingHavoc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gndn import views as gndn_views
from main import views as main_views

urlpatterns = [
    path("",include("main.urls")),
    path("", main_views.home, name="home"),
    # path('admin/', admin.site.urls)
    #gndn
    path('register/', gndn_views.register, name='register_user'),
    path('logout/',gndn_views.logout, name='logout'),
    path('login/',gndn_views.login, name='login')

]

urlpatterns += staticfiles_urlpatterns()
