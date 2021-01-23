# _*_ coding: utf8 _*_

import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def ipaddr(request):
    context = {}
    real_ip = request.META['REMOTE_ADDR']
    forwarded_for_ip = request.META['HTTP_X_FORWARDED_FOR']
    context['ipaddr'] = forwarded_for_ip
    return render(request, 'ipaddr.html', context)
