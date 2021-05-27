from django.http import HttpRequest
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def resourse(request):

    return render(request, 'main/resourse.html')


def registration(request):

    return render(request, 'main/registration.html')
