from django.shortcuts import render, redirect

from .models import Item

# Create your views here.

def home(request):
    return render(request, 'to_do/home.html')

def list_view(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'to_do/list.html', context)