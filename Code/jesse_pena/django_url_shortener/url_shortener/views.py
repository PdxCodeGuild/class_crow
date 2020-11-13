from django.shortcuts import render, redirect
from .models import Shortener
# from django.views.generic.detail import DetailView

import string 
import random
# Create your views here.

def home(request):
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    shorteners = Shortener.objects.all()
    if request.method == 'GET':
        
        context = {
            'shorteners': shorteners,
            'random_string': random_string
        }
        return render (request, 'url_shortener/home.html', context)
    elif request.method == 'POST':
        shortened_url = request.POST['shortened_url']
        if Shortener.objects.all().filter(shortened_url = shortened_url).exists():
        # if shortened_url.exists:
            singular_url = Shortener.objects.get(shortened_url = shortened_url)
            singular_url.count = singular_url.count + 1
            singular_url.save()
        else:
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
    website = 'http://' + shorteners.shortened_url
    return redirect(website)

