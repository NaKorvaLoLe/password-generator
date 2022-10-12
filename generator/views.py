from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', ) #рендер домашней страницы

def info(request):
    return render(request, 'generator/about.html', ) #рендер инфо страницы

def password(request):
    characters=list('abcdefghiklmnopqrstuvwxyz')#список для рандомного выбора

    if request.GET.get('uppercase'):#Условие если стоит галочка для верхнего регистра
        characters.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))#Добавляется список для рандомного выбора буквы в верхнем регистре
    if request.GET.get('special'):  # Условие если стоит галочка для специальныых знаков
        characters.extend(list('!"№;%:?*()'))  # Добавляется список для рандомного выбора знаков
    if request.GET.get('numbers'):  # Условие если стоит галочка для цифр
        characters.extend(list('1234567890'))  # Добавляется список для рандомного выбора цифр

    length = int(request.GET.get('length',12))# Получаем значений из HTML файла из select(name='length)

    thepassword = ''#сюда добавиться случайные значения

    for x in range(length):
        thepassword+= random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


