#coding:utf-8
from django.http import HttpResponse

def home(requst):
    return HttpResponse( 'myApp' )