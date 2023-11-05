from django.contrib import admin
from django.urls import path
from Authentication import views

urlpatterns = [
    path('',views.home,name="home"),
    path('registration/',views.registration,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),


]