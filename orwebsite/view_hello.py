# _*_ coding: utf8 _*_


from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world, Hello Django!")

