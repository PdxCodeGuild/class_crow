from rest_framework import generics 
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Todo 
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset= Todo.objects.all()
    serializer_class = TodoSerializer 

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def home(request):
    return render(request, 'todos/index.html')