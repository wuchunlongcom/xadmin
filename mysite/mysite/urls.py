# -*- coding: utf-8 -*-

from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path(r'admin/', admin.site.urls),
]

# ------------------------------------------------------------------------
# 下面的代码启用 xadmin
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns += [
    path('app/',include('app.urls')),

    path(r'', xadmin.site.urls),
   
    
]
