from django.shortcuts import render, redirect
from datetime import datetime

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

def add_item(request):
    #  incorporate if/elif from add_movie
    if request.method == 'GET':
        items = Item.objects.all()
        context = {
            'items': items
        }
        return render (request, 'list/add_item.html', context)
    elif request.method == 'POST':
        to_do_item = request.POST['to_do_item']
        # created_date = datetime.now
        # completed = False
        newItem = Item.objects.create(
            to_do_item = to_do_item,
            # created_date = created_date,
            # completed = completed
        )
        return redirect('list_view')