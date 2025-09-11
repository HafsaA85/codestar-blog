from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from django.http import HttpResponse # pyright: ignore[reportMissingModuleSource]

# Create your views here.
def index(request):
    return HttpResponse("Hello, blog!")
