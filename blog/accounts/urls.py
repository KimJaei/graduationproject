from django.contrib import admin
from django.urls import path, include
from . import views


# project urls.py에 import include
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]