
from django.urls import path
from . import views

app_name = 'Posts'
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery')
]