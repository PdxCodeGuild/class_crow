from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo 
from .serializers import TodoSerializer

# class ListTodo(APIView):
#     queryset= Todo.objects.all()
#     serializer_class = TodoSerializer
#     def get(self, request, format=None):
#         return Response(data)
    
#     def post(self, request, format=None):
#         return Response()

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def api_list(request):
    if request.method =='GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def home(request):
    return render(request, 'todos/index.html')