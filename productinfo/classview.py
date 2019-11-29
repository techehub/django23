from django.views import  View
from django.http import  HttpResponse

class MyView(View):

    def get(self, request):
        return HttpResponse("Hello")

    def head(self, request):
        res =  HttpResponse("Hello")
        res['name']= "Vijeesh"
        res['contentLength']= 100
        res['content-Type'] = "application/json"
        return res


