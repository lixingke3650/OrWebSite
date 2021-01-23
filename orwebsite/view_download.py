# _*_ coding: utf8 _*_

#std
import os

#
from django.http import HttpResponse, Http404
from django.http import FileResponse
from django.shortcuts import render


DOWNLOAD_DIR = './download'
HIDEFILE = ['.gitkeep',]

def download_list(request):
    filelist = {} #name:url
    context = {}

    list = os.listdir(DOWNLOAD_DIR)
    for filename in list:
        if filename in HIDEFILE:
            continue

        file = os.path.join(DOWNLOAD_DIR, filename)
        if os.path.isfile(file):
            filelist[filename] = os.path.join('../', DOWNLOAD_DIR, filename)

    context['filelist'] = filelist

    return render(request, 'download.html', context)

def download(request, filename):
    file = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.isfile(file):
        with open(file, 'rb') as fd:
            response = HttpResponse(fd.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file)
            return response
    raise Http404
