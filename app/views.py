from django.shortcuts import render
from .forms import SignUpForm


def login(request):
    return render(request, 'app/login.html', {})


def signup(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            
    return render(request, 'app/signup.html', {})
