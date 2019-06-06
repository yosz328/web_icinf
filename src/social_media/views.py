from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_media(request):
	return HttpResponse('derp')

def facebook(request):
	return HttpResponse('fb')