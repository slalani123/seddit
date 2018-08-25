from django.conf.urls import url
from django.contrib import admin
from main import views

from django.urls import path

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^$', views.gaming, name='gaming'),
  path('main/gaming.html', views.gaming),
  url(r'^$', views.humor, name='humor'),
  path('main/humor.html', views.humor),
  url(r'^$', views.programing, name='programing'),
  path('main/programing.html', views.programing),
  url(r'^$', views.tech, name='tech'),
  path('main/tech.html', views.tech),
  url(r'^$', views.login, name='login'),
  path('main/login.html', views.login),
]
