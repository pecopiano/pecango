from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context_dict = {'boldtext': 'This is supposed to be bold'}
#	return HttpResponse('Hello <a href="/rango/about">About</a>')
	return render(request, 'rango/index.html', context_dict)

def about(request):
#	return HttpResponse('About <a href="/rango">Root</a>')
	context_dict = {'aboutmessage': 'Dream for ever'}
	return render(request,'rango/about.html', context_dict)