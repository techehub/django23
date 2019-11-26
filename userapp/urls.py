

from django.contrib import admin
from django.urls import path
from .views import home, login, register,contactPage, saveContact

urlpatterns = [
    path('home', home),
    path('login', login),
    path('reg', register),
    path ('contact', contactPage),
    path('saveContact', saveContact)
]
