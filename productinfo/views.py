from django.shortcuts import render

# Create your views here.

from django.template import loader

from django.http import HttpResponse

def displayProduct(request,id):



    template=loader.get_template("product.html")

    data ={

        "1": {
             "name" : "IPhone",
            "desc" : "This is iPhone 6 smart phone",
            "price" : 55000
        },

        "2": {
            "name": "OPPO",
            "desc": "This is OPPO A5 smart phone",
            "price": 23000
        }
    }



    res = template.render(data[id], request)
    return HttpResponse(res)
