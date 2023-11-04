from django.contrib import admin
from django.urls import path
from Authentication import views

urlpatterns = [
    path('',views.homes),
]