"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()

# 此文件为工程的url解析器，工程的urls大于blog应用urls的优先级，先执行工程的
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 管理员后台界面
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # 管理员登录
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # 管理员注销
    url(r'^search/', include('haystack.urls')),
    # 进行搜索
    url(r'', include('blog.urls')),
    # 当访问路径为空时，也就是根目录，有blog的urls进行解析
]
