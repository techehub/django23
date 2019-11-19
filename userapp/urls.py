

from django.contrib import admin
from django.urls import path
from .views import home, login, register

urlpatterns = [
    path('home', home),
    path('login', login),
    path('reg', register),
]
