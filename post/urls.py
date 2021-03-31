# coding=utf-8

from django.urls import path, re_path
from django.views.generic.base import RedirectView
from post import views

app_name = 'post'
urlpatterns = [
    path('', views.queryAll, name='home'),
    re_path(r'^page/(\d+)$', views.queryAll, name='pos'),
    re_path(r'^post/(\d+)$', views.detail, name='detail'),
    re_path(r'^category/(\d+)$', views.file_category, name='file_category'),
    re_path(r'^sameMonth/(\d{4})/(\d{2})$', views.same_month, name='sameMonth'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/imgs/logo.ico')),
    re_path(r'^post-comment/(\d+)$', views.post_comment, name='post_comment'),
    re_path(r'^contact/', views.contact, name='contact'),
    re_path(r'^like/',views.like,name='like'),
    re_path(r'^mylike/', views.mylike, name='mylike'),
    re_path(r'^mycomment/', views.mycomment, name='mycomment'),
    re_path(r'^mycollection/', views.mycollection, name='mycollection'),
    re_path(r'^aboutauthor/',views.aboutauthor,name = 'aboutauthor'),
]
