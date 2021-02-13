# _*_ coding: utf8 _*_

#std
import os
import shutil
import time

#extensions
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

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
    slot = request.POST.get('slot')
    rstname = request.POST.get('rst_name')
    if slot == 'save':
        try:
            rstfilefullpath = os.path.join(orwebsiteconf.RST_PATH, rstfilename)
            rstfilecache = os.path.join(orwebsiteconf.RST_PATH, RSTUPDATE_CACHE)
            if os.path.exists(rstfilecache) != True:
                os.makedirs(rstfilecache)
            currenttime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            rstfilefullpathdst = os.path.join(rstfilecache, rstfilename + '_' + currenttime)
            shutil.copyfile(rstfilefullpath, rstfilefullpathdst)

            if rstname != rstfilename:
                os.remove(rstfilefullpath)

            rstfilefullpath = os.path.join(orwebsiteconf.RST_PATH, rstname)
            with open(rstfilefullpath, 'w+') as fd:
                text = request.POST.get('rsttextarea')
                fd.write(text)

            return HttpResponse(f"rst file {rstname} update successful.")
        except Exception as e:
            return HttpResponse(f"rst file {rstname} update failed!")
    elif slot == 'preview':
        try:
            # clean preview dir
            cmd = 'cd ' + orwebsiteconf.BLOG_PATH + ' && rm -rf ' + orwebsiteconf.PREVIEW_PATH + '/*'
            os.system(cmd)
            # save rst
            rstfilefullpath = os.path.join(orwebsiteconf.PREVIEW_PATH, rstfilename)
            if os.path.exists(rstfilefullpath):
                return HttpResponse(f"file {rstfilename} exists, create failed.")
            with open(rstfilefullpath, 'w+') as fd:
                text = request.POST.get('rsttextarea')
                fd.write(text)
            # preview
            cmd = 'cd ' + orwebsiteconf.BLOG_PATH + ' && make preview'
            os.system(cmd)
            return redirect(orwebsiteconf.BLOG_URL + "/preview/")
        except Exception as e:
            return HttpResponse(f"rst file {rstfilename} preview failed! %s" %e)
    else:
        return HttpResponse(f"no action in rstupdate!")

def rstnew(request):
    context = {}
    context['rst_name'] = time.strftime('%Y%m%d_New', time.localtime(time.time())) + '.rst'
    context['rst_text'] = NEWRST_TEMPLATE

    return render(request, 'rstnew.html', context)

def rstnewsave(request):
    slot = request.POST.get('slot')
    if slot == 'save':
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
    elif slot == 'preview':
        try:
            # clean preview dir
            cmd = 'cd ' + orwebsiteconf.BLOG_PATH + ' && rm -rf ' + orwebsiteconf.PREVIEW_PATH + '/*'
            os.system(cmd)
            # save rst
            rstname = request.POST.get('rst_name')
            rsttext = request.POST.get('rsttextarea')
            rstfilefullpath = os.path.join(orwebsiteconf.PREVIEW_PATH, rstname)
            if os.path.exists(rstfilefullpath):
                return HttpResponse(f"file {rstfilename} exists, create failed.")
            with open(rstfilefullpath, 'w+') as fd:
                fd.write(rsttext)
            # preview
            cmd = 'cd ' + orwebsiteconf.BLOG_PATH + ' && make preview'
            os.system(cmd)
            return redirect(orwebsiteconf.BLOG_URL + "/preview/")
        except Exception as e:
            return HttpResponse(f"rst file preview failed! %s" %e)
    else:
        return HttpResponse(f"no action in rstnewsave!")

def htmlbuild(request):
    cmd = 'cd ' + orwebsiteconf.BLOG_PATH + ' && make html'
    os.system(cmd)
    return HttpResponse("executed a rebuild for html.")
