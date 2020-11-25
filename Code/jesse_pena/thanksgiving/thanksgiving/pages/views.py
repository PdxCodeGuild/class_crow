from django.shortcuts import render, redirect
from django.http import HttpResponse
from foodsAPI.models import Food

from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from foodsAPI.serializers import FoodSerializer

# Create your views here.
def home(request):
    # return HttpResponse('HELLO THERE')
    foods = Food.objects.all()
    if request.method == 'GET':
        context = {
            'foods' : foods
        }
        return render (request, 'pages/home.html', context)


    # return render(request, 'pages/home.html')

# THIS HAS NOTHING TO DO WITH THE FRONT END --- BACKEND CODE FOR MANAGING DATA
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def food_api_list(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FoodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailFood(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
