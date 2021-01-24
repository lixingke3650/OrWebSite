# _*_ coding: utf8 _*_

#std
import os
import shutil
import time

#extensions
from django.http import HttpResponse
from django.shortcuts import render

#ori
from . import orwebsiteconf

RSTUPDATE_CACHE = 'rstupdatecache'
NEWRST_TEMPLATE = '''
Title
################

:title: New
:date: 2021-01-01 12:30
:category: 日记
:tags:
:author: Hanbin

------

T1
====

T2
++++

T3
^^^^

End

'''



def rstedit(request, rstfilename):
    context = {}
    rstfilefullpath = os.path.join(orwebsiteconf.RST_PATH, rstfilename)
    with open(rstfilefullpath, 'r+') as fd:
        context['rst_name'] = rstfilename
        context['rst_text'] = fd.read()
        return render(request, 'rstedit.html', context)
    return HttpResponse(f"open {rstfilename} failed.")

def rstlist(request):
    rstfilenamelist = []
    context = {}

    filenamelist = os.listdir(orwebsiteconf.RST_PATH)
    for filename in filenamelist:
        if filename[-4:] != '.rst':
            continue
        if os.path.isfile(os.path.join(orwebsiteconf.RST_PATH, filename)):
            rstfilenamelist.append(filename)
    rstfilenamelist.sort()
    context['rstfilenamelist'] = rstfilenamelist

    return render(request, 'blogrstlist.html', context)

def rstupdate(request, rstfilename):
    try:
        rstfilefullpath = os.path.join(orwebsiteconf.RST_PATH, rstfilename)
        rstfilecache = os.path.join(orwebsiteconf.RST_PATH, RSTUPDATE_CACHE)
        if os.path.exists(rstfilecache) != True:
            os.makedirs(rstfilecache)
        currenttime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        rstfilefullpathdst = os.path.join(rstfilecache, rstfilename + '_' + currenttime)
        shutil.copyfile(rstfilefullpath, rstfilefullpathdst)

        with open(rstfilefullpath, 'w+') as fd:
            text = request.POST.get('rsttextarea')
            fd.write(text)

        return HttpResponse(f"rst file {rstfilename} update successful.")
    except Exception as e:
        return HttpResponse(f"rst file {rstfilename} update failed!")

def rstnew(request):
    context = {}
    context['rst_name'] = time.strftime('%Y%m%d_New', time.localtime(time.time())) + '.rst'
    context['rst_text'] = NEWRST_TEMPLATE

    return render(request, 'rstnew.html', context)

def rstnewsave(request):
    try:
        rstname = request.POST.get('rst_name')
        rsttext = request.POST.get('rsttextarea')
        rstfilefullpath = os.path.join(orwebsiteconf.RST_PATH, rstname)
        if os.path.exists(rstfilefullpath):
            return HttpResponse(f"file {rstname} exists, create failed.")
        with open(rstfilefullpath, 'w+') as fd:
            fd.write(rsttext)
        return HttpResponse(f"file {rstname} create successful.")
    except Exception as e:
        return HttpResponse(f"file {rstname} create failed.")

def htmlbuild(request):
    cmd = 'cd ' + orwebsiteconf.BLOG_PATH + ' && make html'
    os.system(cmd)
    return HttpResponse("executed a rebuild for html.")
