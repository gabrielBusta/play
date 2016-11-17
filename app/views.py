import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm


def login(request):
    return render(request, 'app/login.html', {})


def signup(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            redirect('app.views.login')
        else:
            return HttpResponse('Invalid sign up form!',
                                content_type='text/plain')

    return render(request, 'app/signup.html', {})
