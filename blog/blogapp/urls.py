from django.contrib import admin
from django.urls import path, include
from . import views


# project urls.py에 import include
urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
    path('notice/', views.notice, name="notice"),
    path('result/', views.result, name="result")
]