from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1><marquee>Gowthami is a innocent girl</marquee></h1>')
