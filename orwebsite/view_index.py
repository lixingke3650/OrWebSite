# _*_ coding: utf8 _*_


from django.http import HttpResponse
from django.shortcuts import render

#ori
from . import orwebsiteconf

def index(request):
    context = {}
    context['title'] = 'Hi, Welcome to My Site!'
    context['hello_url'] = '/hello'
    context['static_blog_url'] = orwebsiteconf.BLOG_URL
    context['blogedit_url'] = '/editblog/rstlist'
    context['upload_url'] = '/upload'
    context['download_url'] = '/download_list'
    context['ipaddr_url'] = '/ipaddr'
    context['sharetext_url'] = '/sharetext'

    return render(request, 'index.html', context)
