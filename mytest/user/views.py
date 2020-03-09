from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegister
from django.contrib import messages

def register (request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You are successfully registered")
            return redirect ('user-profile')
    else:
        form = UserRegister()
    return render (request, 'user/register.html',{"form":form})

def profile (request):
    return render (request, 'user/profile.html')