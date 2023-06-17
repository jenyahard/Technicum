import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import News


def index(request: HttpRequest) -> HttpResponse:
    template = 'index.html'
    all_news = list(News.objects.all())
    context = {'news': all_news[::-1]}
    print('all_news = ', all_news)
    return render(request, template, context)


def logout_view(request: HttpRequest):
    logout(request)
    template = 'index.html'
    return render(request, template)


def login_view(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index/')
        else:
            error_message = 'Неверный логин или пароль.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def about_view(request):
    template = 'about.html'
    return render(request, template)


def get_users_and_passwords():
    with open('main_page/logpass.txt', 'r') as file:
        # Десериализуем строку JSON в словарь
        return json.loads(file.read())
