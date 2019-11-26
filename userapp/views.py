from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    return HttpResponse("<h1>This is my home page<h1>")

def login(request):
    return HttpResponse("<h1>This is my login page<h1>")


def register(request):
    return HttpResponse("<h1>This is my register page</h1>")

def contactPage(request):
    template= loader.get_template("contact.html")
    myform = ContactForm()
    data= {"contactForm": myform}
    res=template.render ( data, request)
    return  HttpResponse(res)