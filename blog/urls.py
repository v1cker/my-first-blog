from django.conf.urls import url, include, patterns
from . import views
# 该文件是控制blog这个应用的url控制器文件，所有url解析都会通过该文件来获取views中相应的函数方法。

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # 当访问站点根目录时调取views的post_list方法，也就是主页
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # 博文详情页面，主要是通过跳转进入该页面
    url(r'^post/new/$', views.post_new, name='post_new'),
    # 新建博文页面
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # 便捷博文页面
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    # 草稿箱页面
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    # 发布页面
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    # 删除页面
    url(r'^posts/search/$', views.full_search, name='full_search'),
    # 搜索页面
]
