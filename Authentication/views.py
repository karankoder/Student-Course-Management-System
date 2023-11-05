from django.shortcuts import render,redirect
import re
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
User=get_user_model();

def is_iitbhu_email(email):
    pattern = r".+@iitbhu\.ac\.in$"
    if re.match(pattern, email):
        return True
    else:
        return False
    

def home(request):
    return render(request,'Authentication/home.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        name=request.POST.get('name')
        dept=request.POST.get('department')
        sem=request.POST.get('semester')
        if not is_iitbhu_email(email):
            messages.error(request,"Please enter your institue's email address !")
            return redirect('register')
        if(User.objects.filter(email=email)):
            messages.error(request,"Email already exists !")
            return redirect('register')
        myuser=User.objects.create_user(email,password)
        myuser.first_name=name
        myuser.department=dept
        myuser.semester=sem
        myuser.save()
        messages.success(request,"Your Account has been successfully created.")
        return redirect('/')
    return render(request,'Authentication/registration.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are Successfully logged in !")
            return redirect('home')
        else:
            messages.error(request,"Email or password is incorrect")
            return redirect('login')
    return render(request,'Authentication/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Successfully Logged Out!")
        return redirect('/')
    

# Create your views here.
