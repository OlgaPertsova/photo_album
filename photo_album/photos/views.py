from django.shortcuts import render, redirect
from .models import Photos
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'photos/home.html')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def index(request):
    projects = Photos.objects.all()
    return render(request, 'photos/index.html',
                  {'projects': projects})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'photos/signupuser.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'photos/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': "Уже существует"
                })
        else:
            return render(request, 'photos/signupuser.html', {
                'form': UserCreationForm(),
                'error': "Пароли не совпали"
            })


def loginuser(request):
    if request.method == "GET":
        return render(request, 'photos/loginuser.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'photos/loginuser.html', {
                'form': AuthenticationForm(),
                'error': "Неверные данные"
            })
        else:
            login(request, user)
            return redirect('/')

