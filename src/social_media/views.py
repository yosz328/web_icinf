import tweepy
from django.conf import settings
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index_media(request):
	return HttpResponse('derp')

def facebook(request):
	return HttpResponse('fb')

@csrf_exempt
def twit(request):
	# TODO: try it
	auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
	auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
	api = tweepy.API(auth)
	
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PostSerializer(data=data)
		
		if serializer.is_valid():
			try:
				api.update_status(status = 'messagge')
				serializer.save()
				return JSONResponse(serializer.data, status=201)
			except tweepy.TweepError as error:
				if error.api_code == 187: # duplicated
					content = {'error': 'Tweet duplicated'}
					return JSONResponse(content, status=400)
		
		return JSONResponse(serializer.errors, status=400)
	
	else:
		content = {'error': 'method not implemented'}
		return Response(content, status=status.HTTP_501_NOT_IMPLEMENTED)

def twit_list(request):
	# TODO: implement
	pass
	