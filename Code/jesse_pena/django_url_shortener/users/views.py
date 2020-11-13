from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from url_shortener.models import Shortener

# Create your views here.

User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

def profile(request):
    user = request.user
    urls = Shortener.objects.filter(user = user)
    context = {
        'user': user,
        'urls': urls
    }
    return render(request, 'users/profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        new_user = User(
            username = request.POST['username']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        return redirect('login')
    return render(request, 'users/register.html')