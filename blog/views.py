from django.shortcuts import render
from django.http import HttpResponse


def starting_page(request):
    return HttpResponse("I am here")

def posts(request):
    pass

def post_detail(request):
    pass
