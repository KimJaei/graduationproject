from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mbti/', views.mbti, name="mbti"),
    path('c_result/',views.c_result, name="c_result"),
]