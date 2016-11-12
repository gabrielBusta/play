from django.shortcuts import render


def login(request):
    return render(request, 'app/login.html', {})


def signup(request):
    return render(request, 'app/signup.html', {})
