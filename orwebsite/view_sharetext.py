# _*_ coding: utf8 _*_

import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext

SHARE_FILE_DIR = "./sharetext"
SHARE_FILE_NAME = "text"

ERR_NO      = 0
ERR_OTHER   = -1



def read_sharetext():
    err = ERR_NO
    bufferfile = os.path.join(SHARE_FILE_DIR, SHARE_FILE_NAME)
    try:
        if (os.path.isfile(bufferfile) != True):
            str_val = ""
        else:
            with open(bufferfile, 'r') as fd:
                str_val = fd.read()
    except Exception as e:
        str_val = None
        err = ERR_OTHER
    return err, str_val

def write_sharetext(str_val):
    err = ERR_NO
    try:
        with open(os.path.join(SHARE_FILE_DIR, SHARE_FILE_NAME), 'w') as fd:
            fd.write(str_val)
    except Exception as e:
        err = ERR_OTHER
    return err

def sharetext(request):
    context = {}

    err, context['share_text'] = read_sharetext()
    if err == ERR_NO:
        return render(request, 'sharetext.html', context)
    else:
        return HttpResponse('Error: read share file failed.')

def sharetext_save(request):
    try:
        if request.method == "POST":
            form = request.POST
            text = form.get('sharetextarea')
            err = write_sharetext(text)
            if err == ERR_NO:
                return HttpResponse('text save successful.')
            else:
                return HttpResponse('Error: sharetext write failed.')
        else:
            return HttpResponse('Error: request method not is POST.')
    except Exception as e:
        return HttpResponse('Error: sharetext save failed: ' + str(e))
