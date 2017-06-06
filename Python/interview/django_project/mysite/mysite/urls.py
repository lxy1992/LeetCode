# -*- coding: UTF-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""



from django.conf.urls import include, url
from django.contrib import admin

from . import views
# from articles import views as articles_views

urlpatterns = [

    # url(regex, view, kwargs, name) 前两者为必须的参数
    # regex是正则表达式，用于发现匹配的页面，但是由于其不会检索URL中的GET
    # 和POST参数和域名，因此/myapp/和/myapp/?page=3都等于myapp/

    # 匹配到正则表达式后，就会调用view参数指定的视图函数，并将HttpRequest作为第一个参数

    # kwargs任何关键字参数都可以以字典的形式传递给目标的视图

    # name 命名URL，仅修改一个文件就可以改变全局的URL模式


    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.home),
    # url(r'^articles/', articles_views.latest_article),
    # namespace 创建ming'mi
    url(r'^polls/', include('polls.urls', namespace="polls")),

]
