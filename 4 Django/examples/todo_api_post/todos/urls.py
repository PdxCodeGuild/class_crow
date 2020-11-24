from django.urls import path 

from .views import DetailTodo
from . import views

urlpatterns = [
    path('<int:pk>', DetailTodo.as_view()),
    path('', views.api_list, name='list'),
    path('home/', views.home, name='home')
]

