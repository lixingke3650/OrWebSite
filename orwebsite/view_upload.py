# _*_ coding: utf8 _*_

import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf import settings

UPLOAD_DIR = str(settings.BASE_DIR) + '/upload'
DOWNLOAD_DIR = str(settings.BASE_DIR) + '/download'

def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def upload(request):
    context = {}
    return render(request, 'upload.html', context)

def upload_file(request):
    if request.method == "POST":
        myFile = request.FILES.get("upfile", None)
        # check upload file
        if not myFile:
            return HttpResponse("Error: please select a file.")
        # check dir
        if os.path.exists(UPLOAD_DIR) != True:
            os.makedirs(UPLOAD_DIR)
        # file exist already
        destfilename = os.path.join(UPLOAD_DIR, myFile.name)
        if (os.path.isfile(destfilename) == True):
            return HttpResponse("Error: file is exist.")
        # write file
        with open(os.path.join(UPLOAD_DIR, myFile.name), 'wb+') as fd:
            for chunk in read_in_chunks(myFile):
                fd.write(chunk)
        os.symlink(destfilename, os.path.join(DOWNLOAD_DIR, myFile.name))
        return HttpResponse("Upload successful, You can download now.")
    else:
        return HttpResponse("Error: request method not is POST.")
