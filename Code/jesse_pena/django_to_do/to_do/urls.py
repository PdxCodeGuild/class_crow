from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.list_view, name='list_view'),
    path('add_item', views.add_item, name='add_item'),
    
]

