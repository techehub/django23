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


def addToCart(request):
    print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    id = request.GET['pid']
    qty = request.GET['qty']

    cartItems = {}

    if request.session.__contains__("cart"):
        cartItems = request.session['cart']

    cartItems[id] = qty
    request.session['cart'] = cartItems
    print(request.session['cart'])
    return HttpResponse("Added Item to Cart")


def viewCart (request):
    template = loader.get_template("cart.html")
    if request.session.__contains__("cart"):
        cartItems = request.session['cart']

        items= []
        for x,y in cartItems.items():
            p =Product.objects.get(id=x)
            items.append ({"id": x,
                            "qty": y,
                            "name": p.name ,
                            "price": p.price,
                            "total" : p.price * int(y)
                            })

        data ={"products": items}

        res = template.render(data, request)
        return HttpResponse(res)
    else :
        return HttpResponse("Your Cart is Empty")


def writeCookie (req):

    res = HttpResponse("Testing")
    res.set_cookie("TEST_COOKIE", "VIJEESH")
    res.set_cookie("TEST_EMAIL", "vijeesh.tp@expertzlab.com")
    return res;


def readCookie (req):

    val = req.COOKIES['TEST_EMAIL']
    res = HttpResponse(val)
    return res


