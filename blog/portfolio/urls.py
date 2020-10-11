from django.contrib import admin
from django.urls import path, include
from . import views

# project urls.py에 import include
urlpatterns = [
    path('portfolio/', views.portfolio, name="portfolio"),
]