#视图类
#jkCodic 11.15   create

# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context[' hello '] = 'Hello World!'
    return render(request, 'hello.html', context)  #不起作用
	#return HttpResponse('Hello World')