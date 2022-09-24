from django.urls import path, re_path
from django.contrib import admin
from django import urls


from app1 import views


urlpatterns = [

    #contents related urls.

    # re_path(r'^(?P<path>.*)/$', views.home,name='home'),
    path('', views.home, name='home'),
    path('virals/', views.virals, name='virals'),
    path('movies/', views.movies, name='movies'),
    path('webshows/', views.webshows, name='webshows'),
    path('shortfilms/', views.shortfilms, name='shortfilms'),
    path('about/', views.about, name='about'),

    # ==================================================================================

    #authentication  related url

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),



]
