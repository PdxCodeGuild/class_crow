from django.shortcuts import render, redirect
from .models import Shortener
# from django.views.generic.detail import DetailView

import string 
import random
# Create your views here.

def home(request):
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    if request.method == 'GET':
        shorteners = Shortener.objects.all()
        context = {
            'shorteners': shorteners,
            'random_string': random_string
        }
        return render (request, 'url_shortener/home.html', context)
    elif request.method == 'POST':
        shortened_url = request.POST['shortened_url']
        new_url = Shortener.objects.create(
            shortened_url = shortened_url,
            random_string_database = random_string

        )
        return redirect('home')

    return render(request, 'url_shortener/home.html')
    # return redirect()

def list_view(request):
    shorteners = Shortener.objects.all()
    context = {
        'shorteners': shorteners
    }
    return render(request, 'url_shortener/list.html', context)

def detail_view(request, id):
    shorteners = Shortener.objects.get(id=id)
    # context = {
    #     'shorteners': shorteners,
    #     # 'random_string': random_string
    # }

    # context['data'] = Shortener.objects.get(id = id)
    website = 'http://' + shorteners.shortened_url
    # console.log(shorteners)

    # return render(request, 'url_shortener/detail_view.html', context)
    return redirect(website)