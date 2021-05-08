from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse

# Create methods and link urls to methods.

# Create your views here. Render/return data to the webpage itself by returning JSON.


def home(request: HttpRequest):
    return JsonResponse({"msg": "Hello World"})



