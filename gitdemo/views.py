#coding=utf-8
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello github')

def index_view2(request):
    return HttpResponse('hello github')