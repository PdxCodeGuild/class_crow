from django.urls import path 

from .views import ListTodo, DetailTodo
from . import views

urlpatterns = [
    path('<int:pk>', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('home/', views.home, name='home')

]

