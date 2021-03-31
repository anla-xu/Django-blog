#coding=utf-8

from django.urls import path,re_path
from django.views.generic.base import RedirectView
from useroperation import views

app_name = 'useroperation'

urlpatterns = [
    path('',views.logins,name = 'login'),
    re_path('^logining',views.user_login,name = 'logining'),
    re_path('^logout',views.user_logout,name = 'logout'),
    re_path('^register',views.user_register,name = 'register'),
    re_path('^findpwd',views.findpwd, name='findpwd'),
    re_path('^send_email',views.send_email,name = 'send_mail'),
]