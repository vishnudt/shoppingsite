from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
from accounts.models import data



def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password==password2:
            x=data(name=name,email=email,password=password,password2=password2)
            x.save()
        else:
            print('please enter valid')
            return redirect("register")
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('register')
        else:
            messages.info(request,'invalid details')
            return redirect('/')
    else:
        return render(request,'login.html')