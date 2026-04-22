from django.shortcuts import render, redirect
from django.contrib import messages
# Rename the login import to 'auth_login' to avoid conflict with your function name
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .models import Profile

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found')
            return redirect('register') 
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified')
            return redirect('login') 

        user = authenticate(request, username=email, password=password)
        if user:
            auth_login(request, user) 
            return redirect('/') 
        
        messages.success(request, 'Invalid credentials')
        return redirect('login') 
        
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        User.objects.filter(username=email).exists()
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('register')

        user_obj = User.objects.create(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            username=email
        )
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'register.html')

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/') 
    except Exception as e:
        print(e)
        messages.warning(request, 'Invalid token')
        return redirect('register')