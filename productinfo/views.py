from django.shortcuts import render

# Create your views here.

from django.template import loader

from django.http import HttpResponse

from .models import Product

def displayProduct(request,id):

    template=loader.get_template("product.html")
    product = Product.objects.get (id=id)

    data = {"id": product.id,
            "name": product.name,
            "desc": product.desc,
            "price": product.price}

    res = template.render(data, request)
    return HttpResponse(res)

def myProducts(request):
    template = loader.get_template("myproducts.html")
    products = Product.objects.all()
    mydata = {"products":  products}
    res = template.render(mydata, request)
    return HttpResponse(res)
