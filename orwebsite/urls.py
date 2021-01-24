"""orwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#ori
from . import view_hello
from . import view_editblog
from . import view_upload
from . import view_download
from . import view_index
from . import view_ipaddr
from . import view_sharetext

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index.index),
    path('index', view_index.index),
    path('hello/', view_hello.hello),
    path('editblog/rstlist/', view_editblog.rstlist),
    path('editblog/rstnew', view_editblog.rstnew),
    path('editblog/rstnewsave', view_editblog.rstnewsave),
    path('editblog/htmlbuild', view_editblog.htmlbuild),
    path('editblog/rstupdate/<str:rstfilename>', view_editblog.rstupdate),
    path('editblog/rstlist/<str:rstfilename>', view_editblog.rstedit),
    path('upload/', view_upload.upload),
    path('upload_file/', view_upload.upload_file),
    path('download_list/', view_download.download_list),
    path('download/<str:filename>/', view_download.download),
    path('ipaddr/', view_ipaddr.ipaddr),
    path('sharetext/', view_sharetext.sharetext),
    path('sharetext_save/', view_sharetext.sharetext_save),
]
