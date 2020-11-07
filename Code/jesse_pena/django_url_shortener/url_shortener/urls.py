from django.urls import path

from . import views

urlpatterns = [
    # route where it's going to be, function that it will run at the route, name that can be used to reference that path
    path('', views.home, name='home'),
    path('list', views.list_view, name='list_view'),
    path('<id>', views.detail_view, name='detail_view')
]