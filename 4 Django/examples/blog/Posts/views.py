from django.shortcuts import render
from Posts.models import Joke
# Create your views here.

def home(request):
    import random
    name = "Sarah"
    favNumber = random.randint(1, 10)
    favFoods = ['chocolate', 'chiabatta', 'pecans']
    context = {
        'name': name,
        'favNumber': favNumber,
        'favFoods': favFoods,
    }
    return render(request, 'Posts/home.html',context)

def gallery(request):
    jokes = Joke.objects.all()
    joke = Joke.objects.filter(category='animal')
    display = False
    photos = [
        {'url': 'https://cdn.pixabay.com/photo/2020/10/14/01/40/bird-5653140_960_720.jpg', 'alt':'parrot'},
        {'url':'https://cdn.pixabay.com/photo/2020/10/23/16/43/vicuna-5679264_960_720.jpg', 'alt':'baby llama'},
        {'url':'https://media.istockphoto.com/photos/close-up-cute-little-dog-lying-on-picnic-blanket-with-variety-of-picture-id1257438962', 'alt':'dog burrito'}
    
    ]
    context = {
        'jokes': jokes,
        'photos': photos,
        'display': display
    }
    return render (request, 'Posts/gallery.html', context)