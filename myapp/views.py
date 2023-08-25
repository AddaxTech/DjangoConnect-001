from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Account

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        username = first_name[0] + last_name.lower()
        return render(request, 'index.html', {"username":username})
    else:
        return redirect('login')
  

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('/')
        else: 
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':

        first_name = request.POST['fname']
        last_name = request.POST['lname']
        
        email = request.POST['email']
        username = email
        password = request.POST['password']
        
        if first_name or last_name or email or password is "":
            messages.info(request, 'Please fill in all required fields')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Used')
            return redirect ('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')
    
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')