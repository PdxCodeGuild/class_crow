from django.conf.urls import url
from . import views
from django.urls import path

app_name = '<app name>'
urlpatterns = [
    path('', views.home, name='home')
    # path('/about', views.about, name='about')
]