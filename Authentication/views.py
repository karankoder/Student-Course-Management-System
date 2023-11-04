from django.shortcuts import render


def homes(request):
    return render(request,'Authentication/home.html')

# Create your views here.
