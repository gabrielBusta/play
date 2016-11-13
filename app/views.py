from django.shortcuts import render
from django.contrib.auth.models import User

def login(request):
    return render(request, 'app/login.html', {})


def signup(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        
        # TODO: add password validation
        if request.POST.get('password1') == request.POST.get('password2'):
            password=request.POST.get('password1')
        
        user= User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        
    return render(request, 'app/signup.html', {})
