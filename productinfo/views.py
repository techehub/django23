from django.shortcuts import render

# Create your views here.

from django.template import loader

from django.http import HttpResponse

data = {
    "1": {
        "id" : "1",
        "name": "IPhone",
        "desc": "This is iPhone 6 smart phone",
        "price": 55000
    },
    "2": {
        "id" : "2",
        "name": "OPPO",
        "desc": "This is OPPO A5 smart phone",
        "price": 23000
    },
    "3": {
        "id" :"3",
        "name": "SAMSUNG",
        "desc": "This is SAMSUNG smart phone",
        "price": 25000
    }
}

def displayProduct(request,id):

    template=loader.get_template("product.html")


    res = template.render(data[id], request)
    return HttpResponse(res)

def myProducts(request):
    template = loader.get_template("myproducts.html")

    mydata = {"products":  [{
        "id" : "1",
        "name": "IPhone",
        "desc": "This is iPhone 6 smart phone",
        "price": 55000
    },
        {
            "id": "2",
            "name": "OPPO",
            "desc": "This is OPPO A5 smart phone",
            "price": 23000
        },
        {
            "id": "3",
            "name": "SAMSUNG",
            "desc": "This is SAMSUNG smart phone",
            "price": 25000
        }
                            ]}
    res = template.render(mydata, request)
    return HttpResponse(res)
